from django.db import models
from django.utils.translation import gettext_lazy as _
from django_unixdatetimefield import UnixDateTimeField

from teachbaseclient.apps.courses.models.mixins import (
    TrackingFieldsMixin
)


class Author(TrackingFieldsMixin, models.Model):
    """ Модель автора курса """

    name = models.TextField(
        verbose_name=_("first name"),
    )

    email = models.TextField(
        verbose_name=_("email")
    )

    phone = models.TextField(
        verbose_name=_("phone")
    )

    last_name = models.TextField(
        verbose_name=_("last name")
    )

    auth_type = models.IntegerField(
        verbose_name=_("auth type")
    )

    last_activity_at = UnixDateTimeField(
        verbose_name=_("last activity at")
    )

    is_active = models.BooleanField(
        verbose_name=_("is active")
    )

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")
