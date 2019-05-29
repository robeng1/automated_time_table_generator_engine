from flask import jsonify
from flask_restful import Resource, reqparse
from .models import UserModel, RevokedTokenModel, ModuleModel, SectionModel
from .parser import moduleParser, sectionParser
from . import status
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt,
)

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


# TODO: test


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
        except IOError:
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


class ModuleResource(Resource):

    @staticmethod
    def post(module_id=None):
        if module_id:
            return
        # parses the request argument
        data = moduleParser.parse_args(strict=True)

        # initializes a new module
        new_module = ModuleModel()
        new_module.code = data['code']
        new_module.name = data['name']
        new_module.teaching = data['teaching']
        new_module.practicals = data['practicals']
        new_module.credit = data['credit']
        new_module.first_examiner = data["first_examiner"]
        new_module.second_examiner = data["second_examiner"]

        # writes the module to the database
        new_module.save_to_db()

        return jsonify(new_module.to_json()), status.HTTP_201_CREATED

    @staticmethod
    def get(code=None):
        if code is None:
            return {
                'error': 'must provide the course code'
            }
        module = ModuleModel.find_module_by_course_code(code)
        return jsonify(module.to_json()), status.HTTP_200_OK


class SectionResource(Resource):
    @staticmethod
    def post():
        data = sectionParser.parse_args()
        new_section = SectionModel()
        new_section.klass = data["klass"]
        new_section.code = data["code"]
        new_section.shared = data["shared"]
        new_section.save_to_db()
        return jsonify(new_section.to_json()), status.HTTP_201_CREATED

    @staticmethod
    def get(klass=None):
        if klass is None:
            return {
                'error': 'must provide the klass identifier'
            }
        section = SectionModel.find_by_klass(klass)
        return jsonify(section.to_json()), status.HTTP_200_OK
