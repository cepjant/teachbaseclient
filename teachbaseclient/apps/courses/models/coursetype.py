from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import (
    TrackingFieldsMixin
)


class CourseType(TrackingFieldsMixin, models.Model):
    """ Модель типа курса """

    name = models.TextField(
        verbose_name=_("name"),
    )

    class Meta:
        verbose_name = _("course type")
        verbose_name_plural = _("course types")
