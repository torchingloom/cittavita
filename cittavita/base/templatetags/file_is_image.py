import imghdr
from django import template

register = template.Library()

@register.filter
def file_is_image(file):
    if imghdr.what(file) in ('jpeg', 'gif', 'png', ):
        return True
    return False


