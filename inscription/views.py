from utils.views import GmapContextMixin
from django.views.generic import TemplateView
from models import *
from utils.views import DetailViewWithGmap


class IndexView(TemplateView, GmapContextMixin):
    template_name = "inscription/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        areas = Area.objects.all()

        context['areas'] = areas

        return context


class InscriptionListView(TemplateView):
    template_name = "inscription/inscription_list.html"

    def get_context_data(self, **kwargs):
        context = super(InscriptionListView,
                        self).get_context_data(**kwargs)

        areas = Area.objects.all()[1:]

        context['areas'] = areas

        return context


class LocationDetailView(DetailViewWithGmap):
    model = Location

    def get_queryset(self):
        queryset = super(LocationDetailView, self).get_queryset()
        queryset = queryset.select_related('area')

        return queryset


class SubLocationDetailView(DetailViewWithGmap):
    model = SubLocation

    def get_queryset(self):
        queryset = super(SubLocationDetailView, self).get_queryset()
        queryset = queryset.select_related('location',
                                           'location__area')

        return queryset


class InscriptionDetailView(DetailViewWithGmap):
    model = Inscription

    def get_queryset(self):
        queryset = super(InscriptionDetailView, self).get_queryset()
        queryset = queryset.select_related('location',
                                           'location__location',
                                           'location__location__area')
        queryset = queryset.prefetch_related('photos')

        return queryset
