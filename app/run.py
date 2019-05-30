import os

from flask_jwt_extended import JWTManager
from app import app, db, api
from app.models import RevokedTokenModel
from app.resources import (
    UserRegistration, UserLogin, UserLogoutAccess,
    UserLogoutRefresh, TokenRefresh,AllUsers,SecretResource,
    ModuleResource, AllModules
)


@app.before_first_request
def create_tables():
    db.create_all()


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
api.add_resource(SecretResource, '/secret')
api.add_resource(ModuleResource, '/module')
api.add_resource(AllModules, '/modules')

if __name__ == '__main__':
    app.run(debug=True)
