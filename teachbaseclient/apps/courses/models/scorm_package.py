from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import (
    SectionBasedModelMixin
)


class ScormPackage(SectionBasedModelMixin, models.Model):

    name = models.TextField(
        verbose_name=_("name")
    )

    description = models.TextField(
        verbose_name=_("description")
    )

    score = models.IntegerField(
        verbose_name=_("score")
    )

    resource_url = models.TextField(
        verbose_name=_("resource url")
    )

    attachment_status = models.TextField(
        verbose_name=_("attachment status")
    )

    class Meta:
        verbose_name = _("scorm package")
        verbose_name_plural = _("scorm packages")
