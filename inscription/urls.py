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
                           LocationDetailView.as_view(),
                           name='location_detail'),
                       url(r'^sublocation/(?P<pk>\d+)$',
                           SubLocationDetailView.as_view(),
                           name='sublocation_detail'),
                       url(r'^inscription/(?P<pk>\d+)$',
                           InscriptionDetailView.as_view(),
                           name='inscription_detail'),
                       )
