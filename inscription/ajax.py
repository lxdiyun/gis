from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from models import Location, SubLocation, Inscription


@dajaxice_register
def display_location(request, location_id):
    pid = int(location_id)
    location = None

    try:
        location = Location.objects.get(id=pid)
    except ObjectDoesNotExist:
        location = None

    render = render_to_string('inscription/intra_location_info.html',
                              {'location': location})

    dajax = Dajax()
    dajax.assign('#location_info', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def display_sub_location(request, sub_location_id):
    pid = int(sub_location_id)
    sub_location = None

    try:
        sub_location = SubLocation.objects.get(id=pid)
    except ObjectDoesNotExist:
        sub_location = None

    render = render_to_string('inscription/intra_sub_location_info.html',
                              {'sub_location': sub_location})

    dajax = Dajax()
    dajax.assign('#sub_location_info', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def display_inscription(request, inscription_id):
    pid = int(inscription_id)
    inscription = None
    photos = None

    try:
        inscription = Inscription.objects.get(id=pid)
    except ObjectDoesNotExist:
        inscription = None

    if inscription is not None:
        photos = inscription.photos.all()

    render = render_to_string('inscription/intra_inscription_info.html',
                              {'inscription': inscription,
                               'photos': photos})

    dajax = Dajax()
    dajax.assign('#inscription_info', 'innerHTML', render)
    return dajax.json()
