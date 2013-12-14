from django.conf.urls import patterns, url
from utils.views import DetailViewWithGmap
from models import *
from views import *


urlpatterns = patterns('',
                       url(r'^$',
                           IndexView.as_view(),
                           name='inscription_index'),
                       url(r'^area/(?P<pk>\d+)$',
                           DetailViewWithGmap.as_view(model=Area),
                           name='area_detail'),
                       url(r'^location/(?P<pk>\d+)$',
                           DetailViewWithGmap.as_view(model=Location),
                           name='location_detail'),
                       url(r'^sublocation/(?P<pk>\d+)$',
                           DetailViewWithGmap.as_view(model=SubLocation),
                           name='sublocation_detail'),
                       url(r'^inscription/(?P<pk>\d+)$',
                           DetailViewWithGmap.as_view(model=Inscription),
                           name='inscription_detail'),
                       )
