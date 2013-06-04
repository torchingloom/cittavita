# -*- coding: utf-8 -*-

import os

os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

from dev import *

SESSION_ENGINE = 'redis_sessions.session'
INSTALLED_APPS = INSTALLED_APPS + ('cacheops', )
