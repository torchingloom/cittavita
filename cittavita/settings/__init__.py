# -*- coding: utf-8 -*-

ENV_NAME = r'dev'
try:
    from .._ENVIRONMENT import ENV_NAME
except ImportError:
    pass

try:
    exec 'from %s import *' % ENV_NAME
except ImportError:
    symscnt = 80
    bordersym = '*'
    print '\n\n\n%s\n%s%s%s' % (bordersym * symscnt, bordersym, ' ' * (symscnt - 2), bordersym)
    for msg in ('Settings module `%s` not found!' % ENV_NAME, 'Please, be careful and think twice'):
        bats = (symscnt - msg.__len__()) / 2 - 1
        print '%s%s%s%s%s' % (bordersym, ' ' * bats, msg, ' ' * bats, bordersym)
    print '%s%s%s\n%s\n\n' % (bordersym, ' ' * (symscnt - 2), bordersym, bordersym * symscnt)
    exit()

try:
    from settings_local import *
except ImportError:
    pass


