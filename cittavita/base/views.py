# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from models import StaticPage
from ..shop import models as shop_models


class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):

        from .middleware.request import get_current_user
        get_current_user().get_basket()

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


class PageView(DetailView):
    model = StaticPage
    template_name = '../templates/page/view.html'
