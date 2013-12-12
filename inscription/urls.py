from django.conf.urls import patterns, url
from django.views.generic import DetailView
from models import *
from views import *


urlpatterns = patterns('',
                       url(r'^$',
                           IndexView.as_view(),
                           name='inscription_index'),
                       url(r'^inscription/(?P<pk>\d+)$',
                           DetailView.as_view(model=Inscription,
                                              context_object_name='inscription'
                                              ),
                           name='inscription_detail'),
                       )
