import logging
from functools import wraps

from flask import jsonify, current_app

logger = logging.getLogger(__name__)


def exports(rule, **options):
    """
    所有 API 都使用这个 decorator
    """
    def decorator(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            logger.debug("API: %s.%s" % (fn.__module__, fn.__name__))
            return fn(*args, **kwargs)

        api_rule = '{}/api{}'.format(current_app.config['APPLICATION_ROOT'], rule)
        endpoint = options.pop('endpoint', api_rule)
        current_app.add_url_rule(api_rule, endpoint, view_func=decorated_view, **options)
        return decorated_view
    return decorator


class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


    def __str__(self):
        return self.message


@current_app.errorhandler(APIException)
def handle_api_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def make_api_response(payload=None, message=None, statusCode=200):
    body = {
        'status': 'ok'
    }

    # status code and message
    if statusCode != 200:
        body['status'] = 'fail'

    if message:
        body['message'] = message

    # payload
    if payload:
        body['payload'] = payload

    return jsonify(body), statusCode

#
# error handlers
#


@current_app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'status': 'fail',
        'err_code': 400,
        'err_msg': '错误的请求'
    }), 400


@current_app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'status': 'fail',
        'err_code': 401,
        'err_msg': '未登陆'
    }), 401


@current_app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'status': 'fail',
        'err_code': 403,
        'err_msg': '没有权限'
    }), 403


@current_app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        'status': 'fail',
        'err_code': 404,
        'err_msg': '服务不存在'
    }), 404


@current_app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'status': 'fail',
        'err_code': 500,
        'err_msg': '出错了'
    }), 500


@current_app.route('/api/ping')
def ping():
    return 'pong'
