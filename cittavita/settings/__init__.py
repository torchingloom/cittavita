# -*- coding: utf-8 -*-

import sys


def bordered_msg(msg_list, bordersym='*', symscnt=80):
    s = '\n\n\n%s\n%s%s%s' % (bordersym * symscnt, bordersym, ' ' * (symscnt - 2), bordersym)
    for msg in msg_list:
        bats = (symscnt - msg.__len__()) / 2 - 1
        s += '\n%s%s%s%s%s\n' % (bordersym, ' ' * bats, msg, ' ' * bats, bordersym)
    s += '%s%s%s\n%s\n\n' % (bordersym, ' ' * (symscnt - 2), bordersym, bordersym * symscnt)
    return s


ENV_NAME = r'dev'
try:
    from .._ENVIRONMENT import ENV_NAME
except ImportError:
    pass

try:
    exec 'from %s import *' % ENV_NAME
    print >> sys.stderr, bordered_msg(['Settings module `%s`!' % ENV_NAME])
except ImportError:
    print >> sys.stderr, bordered_msg(['Settings module `%s` not found!' % ENV_NAME, 'Please, be careful and think twice'])
    exit()

try:
    from settings_local import *
except ImportError:
    pass
