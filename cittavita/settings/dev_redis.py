# -*- coding: utf-8 -*-

from dev import *

SESSION_ENGINE = 'redis_sessions.session'
INSTALLED_APPS = INSTALLED_APPS + ('cacheops', )
