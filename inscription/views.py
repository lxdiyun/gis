from utils.views import GmapContextMixin
from django.views.generic import TemplateView
from models import Area


class IndexView(TemplateView, GmapContextMixin):
    template_name = "inscription/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        areas = Area.objects.all()

        context['areas'] = areas

        return context
