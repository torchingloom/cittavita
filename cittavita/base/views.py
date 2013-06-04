# -*- coding: utf-8 -*-
from django.views.generic import DetailView
from models import Static_Page


class PageView(DetailView):
    model = Static_Page
    template_name = '../templates/page/view.html'
