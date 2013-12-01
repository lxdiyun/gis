from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from models import Location


@dajaxice_register
def display_location(request, location_id):
    pid = int(location_id)
    photos = None
    location = None

    try:
        location = Location.objects.get(id=pid)
    except ObjectDoesNotExist:
        location = None

    render = render_to_string('inscription/intra_location_info.html',
                              {'location': location,
                               'photos': photos})

    dajax = Dajax()
    dajax.assign('#location_info', 'innerHTML', render)
    return dajax.json()
