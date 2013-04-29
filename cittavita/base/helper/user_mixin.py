# -*- coding: utf-8 -*-

from ...shop.helper.basket import BasketAnonymous, BasketUser

class UserMixin(object):
    def is_admin(self):
        return bool(self.groups.filter(name='administrators'))
    def is_member(self):
        if self.is_admin or self.is_moderator:
            return True
        return bool(self.groups.filter(name='members'))
    def display_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
    def get_basket(self):
        return BasketUser()


class AnonymousUserMixin(object):
    def is_admin(self):
        return False
    def is_member(self):
        return False
    def display_name(self):
        self.__unicode__()
    def get_basket(self):
        return BasketAnonymous()

