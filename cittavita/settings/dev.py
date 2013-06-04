# -*- coding: utf-8 -*-

from default import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += ('debug_toolbar', )

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

REDIS_CLI_PATH = '''d:\\TA\\Dropbox\\Dev\\Redis\\redis-cli'''
