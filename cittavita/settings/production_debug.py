from production import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += ('debug_toolbar', )

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )