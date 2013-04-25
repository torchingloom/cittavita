# -*- coding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from models import Item

class ItemView(DetailView):
    model = Item
    template_name = '../templates/item.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ItemView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        retur = super(ItemView, self).get(request, *args, **kwargs)
        return retur
