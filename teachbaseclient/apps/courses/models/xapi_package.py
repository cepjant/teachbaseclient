from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import (
    SectionBasedModelMixin
)


class XAPIPackage(SectionBasedModelMixin, models.Model):

    name = models.TextField(
        verbose_name=_("name")
    )

    position = None
