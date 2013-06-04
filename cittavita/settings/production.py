
from default import *

STATIC_ROOT = '/home/atlantij/webapps/cittavita_static'

#raise BaseException(MEDIA_ROOT)
#raise BaseException(__file__)

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME

DATABASES['default']['NAME'] = 'atlantij_cittavita'
DATABASES['default']['USER'] = DATABASES['default']['NAME']
DATABASES['default']['PASSWORD'] = 'b36b888c'

SESSION_ENGINE = 'redis_sessions.session'
INSTALLED_APPS = INSTALLED_APPS + ('cacheops', )

REDIS_CLI_PATH = '''/home/atlantij/lib/redis-2.6.13/src/redis-cli'''