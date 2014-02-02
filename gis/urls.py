from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf import settings
from django.conf.urls.static import static

#import guppy
#from guppy.heapy import Remote
#Remote.on()

dajaxice_autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'gis.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(dajaxice_config.dajaxice_url,
                           include('dajaxice.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^search/', include('haystack.urls')),
                       url(r'^old_map/', include('old_map.urls')),
                       url(r'', include('inscription.urls')),
                       )


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
