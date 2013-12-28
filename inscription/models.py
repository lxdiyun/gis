from django.db import models
from django.contrib.contenttypes import generic
from django.utils.encoding import smart_unicode
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

from utils.models import PointBase, PhotoBase, random_path_and_rename


class Photo(PhotoBase):
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))


class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    cover = models.ImageField(upload_to=
                              random_path_and_rename('inscription_area_cover'),
                              blank=True,
                              null=True,
                              verbose_name=_('cover'))
    cover_thumbnail = ImageSpecField(source='cover',
                                     processors=[SmartResize(320,
                                                             180)],
                                     format='JPEG',
                                     options={'quality': 60})

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return reverse("area_detail", kwargs={'pk': self.id})


class Location(PointBase):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    area = models.ForeignKey(Area)

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return reverse("location_detail", kwargs={'pk': self.id})


class SubLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return reverse("sublocation_detail", kwargs={'pk': self.id})


class Inscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    location = models.ForeignKey(SubLocation)
    photos = generic.GenericRelation('Photo',
                                     content_type_field='content_type',
                                     object_id_field='object_id')

    def __unicode__(self):
        return smart_unicode(self.name)

    def get_absolute_url(self):
        return reverse("inscription_detail", kwargs={'pk': self.id})
