from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import (
    TrackingFieldsMixin, SectionBasedModelMixin
)


class Material(TrackingFieldsMixin, SectionBasedModelMixin, models.Model):

    name = models.TextField(
        verbose_name=_("name")
    )

    description = models.TextField(
        verbose_name=_("description")
    )

    is_external = models.BooleanField(
        verbose_name=_("is external")
    )

    external_type = models.TextField(
        verbose_name=_("external type")
    )

    has_file = models.BooleanField(
        verbose_name=_("has file")
    )

    extension = models.TextField(
        verbose_name=_("extension")
    )

    file_name = models.TextField(
        verbose_name=_("file name")
    )

    file_content_type = models.TextField(
        verbose_name=_("file content type")
    )

    category = models.TextField(
        verbose_name=_("category")
    )

    file_size = models.IntegerField(
        verbose_name=_("file size")
    )

    size = models.TextField(
        verbose_name=_("size")
    )

    thumb_url = models.TextField(
        verbose_name=_("thumb url")
    )

    view_url = models.TextField(
        verbose_name=_("view url")
    )

    view_url_cors = models.TextField(
        verbose_name=_("view url cors")
    )

    poster_url = models.TextField(
        verbose_name=_("poster url"),
        blank=True,
        null=True
    )

    status_code = models.TextField(
        verbose_name=_("status code")
    )

    status_name = models.TextField(
        verbose_name=_("status name")
    )

    class Meta:
        verbose_name = _("course material")
        verbose_name_plural = _("course materials")
