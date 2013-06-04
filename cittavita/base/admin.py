# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.sites.models import Site
from models import *

admin.site.register(Static_Page)
admin.site.unregister(Site)