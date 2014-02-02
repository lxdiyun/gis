from django.views.generic import TemplateView

from utils.views import GmapContextMixin


class OldMapView(TemplateView, GmapContextMixin):
    template_name = "old_map/old_map.html"
