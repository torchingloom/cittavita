# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView, View
from ..base.helper.view import JSONView
from ..shop import models as shop_models
from models import Item


class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        shelf_width = 896 * 2
        shelfs = ()
        shelfs_num = 1
        context = super(self.__class__, self).get_context_data(**kwargs)
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
    model = Item
    template_name = '../templates/item.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return super(self.__class__, self).get(request, *args, **kwargs)


class ItemAddToBasketView(JSONView):
    add_state = None
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        from ..base.middleware.request import get_current_user
        self.add_state = get_current_user().get_basket().add_item(kwargs.get('pk'), kwargs.get('count'))
        return super(self.__class__, self).dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        kwargs = super(self.__class__, self).get_context_data(**kwargs)
        kwargs.update({'add_status': self.add_state})
        return kwargs