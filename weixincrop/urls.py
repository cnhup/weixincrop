from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^callback/$','weixincrop.views.callback'),
)
