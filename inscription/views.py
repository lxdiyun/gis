from utils.views import GmapViewBase
from models import Area


class IndexView(GmapViewBase):
    template_name = "inscription/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        areas = Area.objects.all()

        context['areas'] = areas

        return context
