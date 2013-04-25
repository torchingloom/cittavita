# -*- coding: utf-8 -*-

import os
from django.contrib import admin
from sorl.thumbnail.shortcuts import get_thumbnail
from models import *

class Item_Image_Border_Admin(admin.ModelAdmin):
    list_display = ('name', 'thumb')

    def thumb(self, instance):
        return '<img src="%(thumb)s" />' % {'thumb': get_thumbnail(instance.image.path, '50x50').url, 'image': instance.image.url}

    thumb.short_description = u'Картинка'
    thumb.allow_tags = True

class Item_Image_Inline(admin.StackedInline):
    model = Item_Image
    extra = 1

class Item_Admin(admin.ModelAdmin):
    inlines = [Item_Image_Inline]
    list_display = ('name', 'thumb')
    search_fields = ('name', 'info')

    def thumb(self, instance):
        try:
            image = instance.get_image()
            return '<img src="%(thumb)s" />' % {'thumb': get_thumbnail(image.image.path, '50x50').url, 'image': image.image.url}
        except Exception:
            return ''

    thumb.short_description = u'Картинка'
    thumb.allow_tags = True

admin.site.register(Item_Image_Border, Item_Image_Border_Admin)
admin.site.register(Item, Item_Admin)
