# -*- coding: utf-8 -*-

import subprocess
from django.core.management.base import BaseCommand
from ....settings import REDIS_CLI_PATH, ENV_NAME


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not REDIS_CLI_PATH:
            symscnt = 80
            bordersym = '*'
            self.stdout.write('\n\n\n%s\n%s%s%s' % (bordersym * symscnt, bordersym, ' ' * (symscnt - 2), bordersym))
            for msg in ('`REDIS_CLI_PATH` has no value!', 'Please, set it & try again, baby'):
                bats = (symscnt - msg.__len__()) / 2 - 1
                self.stdout.write('%s%s%s%s%s' % (bordersym, ' ' * bats, msg, ' ' * bats, bordersym))
            self.stdout.write('%s%s%s\n%s\n\n' % (bordersym, ' ' * (symscnt - 2), bordersym, bordersym * symscnt))
            return
        cmd = '%s -r 1 flushall' % REDIS_CLI_PATH
        subprocess.call(cmd)