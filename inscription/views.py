from utils.views import GmapViewBase
from models import Location


class IndexView(GmapViewBase):
    template_name = "inscription/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        locations = Location.objects.all()

        context['locations'] = locations

        return context
