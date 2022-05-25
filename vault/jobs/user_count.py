from vault import app, db
from vault.models.user import User


def run():
    count = db.session.query(User).count()
    app.logger.info('User count: %d', count)
