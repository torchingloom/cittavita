# -*- coding: utf-8 -*-
from django import template
from ..helper.pluralize import pluralize

register = template.Library()

@register.filter
def pluralize_normal(value, arg):
    return pluralize(value, arg)