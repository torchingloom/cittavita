# -*- coding: utf-8 -*-

import Image
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from sorl.thumbnail.shortcuts import get_thumbnail
from cittavita.shop import item_image_border_filename_generate, item_image_filename_generate
from django.contrib.auth.models import User


class Item(models.Model):
    class Meta:
        verbose_name = u'товар'
        verbose_name_plural = u'товары'

    name = models.CharField(max_length=255, unique=True, db_index=True, verbose_name=u'название товара', help_text=u'Уникальное название товара. Будет фигурировать в ссылке на карточку товара.')
    price = models.FloatField(null=True, verbose_name=u'цена')
    price_old = models.FloatField(null=True, verbose_name=u'старая цена')
    info = models.TextField(null=True, verbose_name=u'информация')
    preview_width = models.IntegerField(null=True, blank=True, verbose_name=u'ширина превьюшки, если нет рамки')
    margin_left = models.IntegerField(default=0, verbose_name=u'отступ слева', help_text=u'Отступ слева от границы стеллажа или от другого товара. Может быть отрицательным.')
    is_exists = models.BooleanField(null=False, default=True, verbose_name=u'в наличии')

    def __unicode__(self):
        return u'%s' % (self.name)

    def get_width(self):
        img = self.get_image()
        if img:
            if img.border:
                if img.border.preview_width:
                    return img.border.preview_width
                return img.border.image.width
            else:
                if self.preview_width:
                    return self.preview_width
                max_height = 200
                return int(round(img.image.width * (float(min(img.image.height, max_height)) * 100 / img.image.height) / 100))
        return 0

    def get_image(self):
        img = self.item_image_set.filter(is_primary=True)
        if img:
            return img[0]
        return None

    def get_front_thumb(self):
        img = self.get_image()
        if img:
            return get_thumbnail(img.image.path, '%s' % self.get_width(), format='PNG')
        return None

    def get_absolute_url(self):
        return r'/#page1-item%s' % self.pk


class Item_Image_Border(models.Model):
    name = models.CharField(max_length=500, verbose_name=u'название рамки')
    image = models.ImageField(upload_to=item_image_border_filename_generate, verbose_name=u'картинка')
    preview_width = models.IntegerField(null=True, blank=True, verbose_name=u'ширина превьюшки для этой рамки')

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        verbose_name = u'рамка для картинки товара'
        verbose_name_plural = u'рамки для картинок товаров'


class Item_Image(models.Model):
    item = models.ForeignKey(Item, null=False, on_delete=models.CASCADE, verbose_name=u'товар')
    thumb_width = models.PositiveIntegerField(null=True, blank=True, verbose_name=u'ширина превьюшки')
    thumb_height = models.PositiveIntegerField(null=True, blank=True, verbose_name=u'высота превьюшки')
    border = models.ForeignKey(Item_Image_Border, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500, verbose_name=u'название картинки')
    info = models.TextField(null=True, verbose_name=u'описание картинки')
    image = models.ImageField(upload_to=item_image_filename_generate, verbose_name=u'картинка')
    is_primary = models.BooleanField(default=False, verbose_name=u'основная')

    def __unicode__(self):
        return u'[%s] %s' % (self.item.name, self.name)

    def get_detail_thumb(self):
        return get_thumbnail(self.image.path, '%sx%s' % (450, 450), format='PNG')

    def get_detail_list_thumb(self):
        return get_thumbnail(self.image.path, 'x%s' % 100, format='PNG')

    class Meta:
        ordering = ['item', '-is_primary']
        verbose_name = u'картинка товара'
        verbose_name_plural = u'картинки товара'


class Basket(models.Model):
    item = models.ForeignKey(Item, null=False, on_delete=models.CASCADE, verbose_name=u'товар')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u'пользователь')
    session_key = models.CharField(max_length=500, db_index=True, null=True, blank=True, verbose_name=u'идентификатор сессии')
    count = models.IntegerField(default=1, verbose_name=u'сколько штук')
    price_one = models.FloatField(verbose_name=u'цена')
    when = models.DateTimeField(auto_now=True, auto_now_add=True, db_index=True, verbose_name=u'когда')
    class Meta:
        unique_together = ['item', 'user', 'session_key']
        verbose_name = u'корзина'
        verbose_name_plural = u'корзины'
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.user:
            row = self.get_row_by_item_and_session_key()
            if row:
                self.pk = row.pk
        return super(self.__class__, self).save(force_insert, force_update, using, update_fields)

    def get_row_by_item_and_session_key(self):
        try:
            return self.__class__.objects.get(item=self.item, session_key=self.session_key)
        except ObjectDoesNotExist:
            return False
