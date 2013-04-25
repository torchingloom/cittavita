
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from cittavita.base.views import HomeView
from cittavita.shop.views import ItemView
from django.contrib.auth.urls import urlpatterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns += patterns('',
    url(r'^$', HomeView.as_view(), name='home-view'),
    url(r'item/(?P<pk>\d+)$', ItemView.as_view(), name='item-view'),
    (r'^admin/', include(admin.site.urls)),
    (r'^shop/', include('shop.urls'))
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
