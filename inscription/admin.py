from django.contrib.gis import admin

from utils.admin import PointAdminBase, PhotoInlineBase
from models import (Area, Location, SubLocation, Inscription, Photo)


class PhotoInline(PhotoInlineBase):
    model = Photo


class InscriptionAppAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


class LocationAdmin(InscriptionAppAdmin, PointAdminBase):
    pass

admin.site.register(Area, InscriptionAppAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(SubLocation, InscriptionAppAdmin)
admin.site.register(Inscription, InscriptionAppAdmin)
#admin.site.register(Photo)
