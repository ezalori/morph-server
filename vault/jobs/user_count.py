import logging

from vault import db
from vault.models.user import User

logger = logging.getLogger(__name__)


def run():
    count = db.session.query(User).count()
    logger.info('Result: %d', count)
