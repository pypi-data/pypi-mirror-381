"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "1.1.0"

PACKAGE_NAME = "cs_flickrgallery"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)


ANNOTATION_KEY = "cs_flickrgallery"
