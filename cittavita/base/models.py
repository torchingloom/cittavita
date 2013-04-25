# -*- coding: utf-8 -*-

from django.db import models

class StaticPage(models.Model):
    STATUS_CHOICES = (
        ('pending', u'На рассмотрении'),
        ('published', u'Опубликована')
    )
    name = models.CharField(max_length=100, primary_key=True, verbose_name=u'идентификатор', help_text=u'Только латинские символы, подчеркивание, тире и точка')
    title = models.CharField(max_length=500, verbose_name=u'название')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, default='published', db_index=True, verbose_name=u'статус')
    created = models.DateTimeField(null=False, auto_now_add=True, verbose_name=u'дата создания')
    last_changed = models.DateTimeField(null=False, auto_now=True, verbose_name=u'дата последнего изменения')
    content = models.TextField(null=True, verbose_name=u'Текст')

    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'

    def __unicode__(self):
        return self.title
