"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "2.0.0a10"

PACKAGE_NAME = "plonegovbr.socialmedia"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
