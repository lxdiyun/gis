from django.db import models
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from utils.models import PointBase, PhotoBase


class Location(PointBase):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))


class SubLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    location = models.ForeignKey(Location)


class Inscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
    location = models.ForeignKey(SubLocation)
    photos = generic.GenericRelation('Photo',
                                     content_type_field='content_type',
                                     object_id_field='object_id')


class Photo(PhotoBase):
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name=_("description"))
