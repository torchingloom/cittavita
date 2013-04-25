
from django.conf.urls.defaults import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^testemail$', TestEmail.as_view(), name='testemail'),
    url(r'^page/(?P<pk>.*)$', PageView.as_view(), name='base-page-view'),
)
