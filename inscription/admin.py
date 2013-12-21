from django.contrib.gis import admin
from django.utils.translation import ugettext_lazy as _
from imagekit.admin import AdminThumbnail

from utils.admin import PointAdminBase, PhotoInlineBase
from models import (Area, Location, SubLocation, Inscription, Photo)


class PhotoInline(PhotoInlineBase):
    model = Photo


class AreaAdmin(admin.ModelAdmin):
    readonly_fields = ['admin_thumbnail']
    admin_thumbnail = AdminThumbnail(image_field='cover_thumbnail')

    admin_thumbnail.short_description = _('Cover Thumbnail')


class InscriptionAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Area, AreaAdmin)
admin.site.register(Location, PointAdminBase)
admin.site.register(SubLocation)
admin.site.register(Inscription, InscriptionAdmin)
#admin.site.register(Photo)
