# -*- coding: utf-8 -*-

from default import *

INSTALLED_APPS += ('debug_toolbar', )

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

REDIS_CLI_PATH = '''d:\\TA\\Dropbox\\Dev\\Redis\\redis-cli'''
