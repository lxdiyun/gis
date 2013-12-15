from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from models import Area, Location, SubLocation, Inscription

MAX_LOCATIONS_ON_INDEX = 15


@dajaxice_register
def display_area(request, area_id):
    area = None
    locations = None

    if area_id is not None:
        id = int(area_id)
        try:
            area = Area.objects.get(id=id)
            if 1 != id:
                locations = area.location_set.all()
            else:
                # randomly get locations at most
                locations = Location.objects.all().order_by('?')
                locations = locations[:MAX_LOCATIONS_ON_INDEX]

        except ObjectDoesNotExist:
            area = None

    render = render_to_string('inscription/intra_area_info.html',
                              {'area': area})
    dajax = Dajax()
    if locations is not None:
        data = serializers.serialize("json", locations)
        dajax.add_data(data, 'add_locations')
    dajax.assign('#area_or_location_info', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def display_location(request, location_id):
    id = int(location_id)
    location = None

    try:
        location = Location.objects.get(id=id)
    except ObjectDoesNotExist:
        location = None

    render = render_to_string('inscription/intra_location_info.html',
                              {'location': location})

    dajax = Dajax()
    dajax.assign('#area_or_location_info', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def display_sublocation(request, sublocation_id):
    id = int(sublocation_id)
    sublocation = None

    try:
        sublocation = SubLocation.objects.get(id=id)
    except ObjectDoesNotExist:
        sublocation = None

    render = render_to_string('inscription/intra_sublocation_info.html',
                              {'sublocation': sublocation})

    dajax = Dajax()
    dajax.assign('#sublocation_info', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def display_inscription(request, inscription_id):
    id = int(inscription_id)
    inscription = None

    try:
        inscription = Inscription.objects.prefetch_related('photos').get(id=id)
    except ObjectDoesNotExist:
        inscription = None

    render = render_to_string('inscription/intra_inscription_info.html',
                              {'inscription': inscription})

    dajax = Dajax()
    dajax.assign('#inscription_info', 'innerHTML', render)
    return dajax.json()
