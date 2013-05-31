# -*- coding: utf-8 -*-

def basket(request):
    from ..base.middleware.request import get_current_user
    return {'basket': get_current_user().get_basket()}