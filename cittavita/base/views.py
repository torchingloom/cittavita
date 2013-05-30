# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from models import StaticPage


class PageView(DetailView):
    model = StaticPage
    template_name = '../templates/page/view.html'
