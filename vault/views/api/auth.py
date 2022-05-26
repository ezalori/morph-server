from flask import request
from flask_login import login_user, logout_user, login_required, current_user

from vault import app
from vault.services import UserService
from vault.views.api import make_api_response, exports, APIException


@exports('/login', methods=['POST'])
def login() -> tuple:
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        raise APIException('Username and password cannot be empty.')

    user = UserService.login(username, password)
    if user is None:
        raise APIException('Invalid username or password.')

    login_user(user)
    app.logger.info(f'{username} Login')

    return make_api_response({
        'id': user.user.id,
        'username': user.user.username,
    })


@exports('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return make_api_response()


@exports('/current-user')
@login_required
def get_current_user():
    return make_api_response(payload={
        'id': current_user.user.id,
        'username': current_user.user.username,
    })
