# -*- coding: utf-8 -*-

from ...base.helper.singleton import singleton
from .. import models
from ...base.middleware.request import get_request, get_current_user


class BasketException(BaseException):
    pass

class Basket(object):
    model = None
    def __init__(self):
        self.get_model_filtered_queryset()
    def get_model_filtered_queryset(self):
        raise BasketException('get_model_filtered_queryset not implemented')

@singleton
class BasketAnonymous(Basket):
    model = models.Basket_Anonymous
    def get_model_filtered_queryset(self):
        return self.model.objects.filter(session_id=get_request().session.session_key)


@singleton
class BasketUser(Basket):
    model = models.Basket_User
    def get_model_filtered_queryset(self):
        return self.model.objects.filter(user=get_current_user())