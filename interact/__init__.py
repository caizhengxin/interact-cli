from __future__ import print_function
import logging.config

from interact import settings


__version__ = "0.1.0"
__author__ = "jankincai"


logging.config.dictConfig(settings.LOGGING)
