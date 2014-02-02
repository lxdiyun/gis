from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
                       url(r'^$',
                           OldMapView.as_view(),
                           name='old_map'),
                       )
