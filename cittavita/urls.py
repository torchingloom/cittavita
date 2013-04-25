
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from cittavita.base import views as base_views
from django.contrib.auth.urls import urlpatterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns += patterns('',
    # url(r'^$', base_views.IndexPageView.as_view(), name='index-view'),
    # url(r'item/(?P<pk>\d+)$', base_views.ItemView.as_view(), name='item-view'),
    (r'^admin/', include(admin.site.urls)),
    # (r'^base/', include('cittavita.base.urls')),
    # (r'^basket/', include('basket.urls'))
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
