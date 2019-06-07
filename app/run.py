from flask_jwt_extended import JWTManager
from app import app, db, api
from app.models import RevokedTokenModel
from app.resources import (
    UserRegistration, UserLogin, UserLogoutAccess,
    UserLogoutRefresh, TokenRefresh, AllUsers,
    CourseResource, ClassRoomResource, ClassRoomGroupResource,
    RoomGroupResource, DepartmentResource, SingleDepartmentResource,
    LecturerResource, SingleLecturerResource, SectionResource, Flat, Timetable
)


@app.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()


jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)


api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
api.add_resource(AllUsers, '/users')
api.add_resource(CourseResource, '/courses')
api.add_resource(ClassRoomResource, '/classrooms')
api.add_resource(ClassRoomGroupResource, '/classroomgroup')
api.add_resource(RoomGroupResource, '/classroomgroup/<name>')
api.add_resource(DepartmentResource, '/departments')
api.add_resource(SingleDepartmentResource, '/departments/<name>')
api.add_resource(LecturerResource, '/lecturers')
api.add_resource(SingleLecturerResource, '/lecturers/<name_or_id>')
api.add_resource(SectionResource, '/sections')
api.add_resource(Flat, '/flat')
api.add_resource(Timetable, '/table')

if __name__ == '__main__':
    app.run(debug=True)
