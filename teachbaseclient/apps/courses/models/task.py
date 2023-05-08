from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import (
    TrackingFieldsMixin, SectionBasedModelMixin
)


class Task(TrackingFieldsMixin, SectionBasedModelMixin, models.Model):

    name = models.TextField(
        verbose_name=_("name")
    )

    description = models.TextField(
        verbose_name=_("description")
    )

    score = models.IntegerField(
        verbose_name=_("score")
    )

    required = models.BooleanField(
        verbose_name=_("required")
    )

    team_passage = models.BooleanField(
        verbose_name=_("team passage")
    )

    allow_incomplete_score = models.BooleanField(
        verbose_name=_("allow incomplete score")
    )

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
