from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from flask_restful import Resource, reqparse
from .models import (
    UserModel, RevokedTokenModel,
    CourseModel, SectionModel,
    ClassRoomGroupModel, ClassRoomModel,
    DepartmentModel, LecturerModel, FlatTimeTableModel
)
from scheduler.timetablegenerator import Gen
from .parser import (
    course_parser, section_parser,
    classroom_group_parser, classroom_parser,
    department_parser, lecturer_parser
)
from . import status
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)
from . import helper

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    @staticmethod
    def post():
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except IOError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR


class UserLogin(Resource):
    @staticmethod
    def post():
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {'message': "User {} doesn't exist".format(data['username'])}

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except IOError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    @staticmethod
    def get():
        return UserModel.return_all()

    @staticmethod
    def delete():
        return UserModel.delete_all()


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }


class CourseResource(Resource):
    @staticmethod
    def post():
        data = course_parser.parse_args(strict=True)
        course = CourseModel()
        course.code = data['code']
        course.name = data['name']
        course.teaching = data['teaching']
        course.practicals = data['practicals']
        course.tutorial = data['tutorial']
        course.credit = data['credit']
        course.first_examiner = data["first_examiner"]
        course.second_examiner = data["second_examiner"] or None
        course.department = data['department']
        if not helper.valid_level(data["year"]):
            return {'message': 'Invalid level'}, status.HTTP_400_BAD_REQUEST
        try:
            course.save_to_db()
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return course.to_json(), status.HTTP_201_CREATED

    @staticmethod
    def get():
        return CourseModel.return_all(), status.HTTP_200_OK


class SectionResource(Resource):
    @staticmethod
    def post():
        data = section_parser.parse_args(strict=True)
        section = SectionModel()
        section.name = data["name"]
        section.department = data["department"]
        section.year = data["year"]
        section.size = data["size"]
        try:
            section.save_to_db()
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return section.to_json(), status.HTTP_201_CREATED

    @staticmethod
    def get():
        return SectionModel.return_all(), status.HTTP_200_OK


class ClassRoomResource(Resource):
    @staticmethod
    def post():
        data = classroom_parser.parse_args(strict=True)
        room = ClassRoomModel()
        room.name = data['name']
        room.capacity = data['capacity']
        room.allowance = data['allowance']
        room.location = data['location']
        room.group = data['group']
        try:
            room.save_to_db()
        except IntegrityError:
            return {'message': "{} already exists".format(data['name'])}, status.HTTP_400_BAD_REQUEST
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return room.to_json(), status.HTTP_201_CREATED

    @staticmethod
    def get():
        return ClassRoomModel.return_all(), status.HTTP_200_OK


class ClassRoomGroupResource(Resource):
    @staticmethod
    def post():
        data = classroom_group_parser.parse_args(strict=True)
        grp = ClassRoomGroupModel()
        grp.name = data['name']
        try:
            grp.save_to_db()
        except IntegrityError:
            return {'message': "{} already exists".format(data['name'])}
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return grp.to_json(), status.HTTP_201_CREATED

    @staticmethod
    def get():
        return ClassRoomGroupModel.return_all(), status.HTTP_200_OK


class RoomGroupResource(Resource):
    @staticmethod
    def get(name=None):
        return ClassRoomGroupModel.find_by_name(name=name)


class DepartmentResource(Resource):
    @staticmethod
    def post():
        data = department_parser.parse_args()
        dep = DepartmentModel()
        dep.name = data['name']
        dep.code = data['code']
        try:
            dep.save_to_db()
        except IntegrityError:
            return {'message': "{} already exists".format(data['name'])}, status.HTTP_400_BAD_REQUEST
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return dep.to_json(), status.HTTP_201_CREATED

    @staticmethod
    def get():
        return DepartmentModel.return_all(), status.HTTP_200_OK


class SingleDepartmentResource(Resource):
    @staticmethod
    def get(name=None):
        if name is None:
            return {'message': "must provide the name of the department"}, status.HTTP_400_BAD_REQUEST
        return DepartmentModel.find_by_name(name=name)


class LecturerResource(Resource):
    @staticmethod
    def post():
        data = lecturer_parser.parse_args()
        lecturer = LecturerModel()
        lecturer.title = data['title']
        lecturer.name = data['name']
        lecturer.stuff_id = data['stuff_id']
        lecturer.email = data['email']
        lecturer.department = data['department']
        lecturer.office = data['office']
        try:
            lecturer.save_to_db()
        except IntegrityError:
            return {'message': "{} already exists".format(data['name'])}, status.HTTP_400_BAD_REQUEST
        except SQLAlchemyError:
            return {'message': 'Something went wrong'}, status.HTTP_500_INTERNAL_SERVER_ERROR
        return lecturer.to_json(), status.HTTP_201_CREATED

    @staticmethod
    def get():
        return LecturerModel.return_all(), status.HTTP_200_OK


class SingleLecturerResource(Resource):
    @staticmethod
    def get(name_or_id=None):
        if name_or_id is None:
            return {'message': "missing argument"}, status.HTTP_400_BAD_REQUEST
        try:
            val = int(name_or_id)
            return LecturerModel.find_by_id(id=val), status.HTTP_200_OK
        except ValueError:
            return LecturerModel.find_by_name(name=name_or_id), status.HTTP_200_OK


class Flat(Resource):
    @staticmethod
    def get():
        return FlatTimeTableModel.return_all()


class Timetable(Resource):
    @staticmethod
    def get():
        pp = Gen()
        return pp.json()
