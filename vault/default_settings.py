APPLICATION_ROOT = ''
SESSION_COOKIE_NAME = 'vault_session'
SECRET_KEY = 'This should be replaced on production'

# API & JSON
JSON_AS_ASCII = False
JSONIFY_PRETTYPRINT_REGULAR = True
JSON_SORT_KEYS = None
FE_ENV = 'development'

# database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1/morph?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
