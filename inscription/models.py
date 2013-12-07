from django.db import models
from django.contrib.contenttypes import generic
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _
from utils.models import PointBase, PhotoBase


class Area(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))

    def __unicode__(self):
        return smart_unicode(self.name)


class Location(PointBase):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    area = models.ForeignKey(Area)

    def __unicode__(self):
        return smart_unicode(self.name)


class SubLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return smart_unicode(self.name)


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


class Photo(PhotoBase):
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
