from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import *


urlpatterns = patterns('',
                       url(r'^$',
                           IndexView.as_view(),
                           name='inscription_index'),
                       url(r'^inscription_list$',
                           InscriptionListView.as_view(),
                           name='inscription_list'),
                       url(r'^about$',
                           TemplateView.as_view(
                               template_name="inscription/about_us.html"),
                           name='about_us'),
                       url(r'^area/(?P<pk>\d+)$',
                           AreaDetailView.as_view(),
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
