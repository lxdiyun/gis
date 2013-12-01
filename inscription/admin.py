from django.contrib.gis import admin
from utils.admin import PointAdminBase, PhotoInlineBase
from models import Location, SubLocation, Inscription, Photo


class PhotoInline(PhotoInlineBase):
    model = Photo


class InscriptionAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Location, PointAdminBase)
admin.site.register(SubLocation)
admin.site.register(Inscription, InscriptionAdmin)
#admin.site.register(Photo)
