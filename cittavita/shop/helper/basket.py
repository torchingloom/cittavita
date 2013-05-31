# -*- coding: utf-8 -*-
import formatter
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Sum
from django.utils.datastructures import SortedDict

from ...base.helper.singleton import singleton
from .. import models
from ...base.middleware.request import get_request, get_current_user


class BasketException(BaseException):
    pass

@singleton
class Basket(object):
    model = models.Basket
    item_model = models.Item
    user = None
    session_key = None

    def __init__(self):
        self.user = get_current_user()
        self.session_key = get_request().COOKIES.get('sessionid')

    def get_item_count(self):
        return self.model.objects.filter(session_key=self.session_key).count()

    def get_total_price(self):
        return self.model.objects.extra(select={'total': 'SUM(count * price_one)'}, where=['session_key=%s'], params=[self.session_key]).values('total')[0].get('total') or 0

    def add_item(self, item_pk, count=1):
        item_in_basket = self.model()
        item_in_basket.item = self.get_item_by_pk(item_pk)
        if not item_in_basket.item:
            return False
        if not isinstance(self.user, AnonymousUser):
            item_in_basket.user = self.user
        item_in_basket.session_key = self.session_key
        item_in_basket.count = count
        item_in_basket.price_one = item_in_basket.item.price
        item_in_basket.save()
        return True

    def get_item_by_pk(self, item_pk):
        try:
            return self.item_model.objects.get(pk=item_pk)
        except ObjectDoesNotExist:
            return False