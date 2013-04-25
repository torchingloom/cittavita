# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from models import *
from ..shop import models as shop_models

class IndexPageView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        shelf_width = 896 * 2
        shelfs = ()
        shelfs_num = 1

        context = super(IndexPageView, self).get_context_data(**kwargs)

        items = shop_models.Item.objects.filter(is_exists=True)

        shelf_current = ()
        shelf_current_width = 0
        for item in items:
            item_width = item.get_width() + item.margin_left
            if shelf_current_width + item_width > shelf_width:
                shelfs += ({'num': shelfs_num, 'items': shelf_current},)
                shelf_current = ()
                shelf_current_width = 0
                item.margin_left = 0
                shelfs_num += 1
            shelf_current += (item,)
            shelf_current_width += item_width

        shelfs += ({'num': shelfs_num, 'items': shelf_current},)

        context.update({'shelfs': shelfs})

        return context


class ItemView(DetailView):
    model = shop_models.Item
    template_name = 'base/item.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ItemView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        retur = super(ItemView, self).get(request, *args, **kwargs)
#        raise BaseException(self.object.item_image_set.)
        return retur


class PageView(DetailView):
    model = StaticPage
    template_name = 'base/page/view.html'


class TestEmail(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        from django.contrib.auth.models import User
        from base.helper.mail import ToUsers
        from django.db.models.query_utils import Q
        m = ToUsers(User.objects.filter(Q(id=1) | Q(id=8)), 'test')
        m.send()