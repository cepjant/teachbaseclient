from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import (
    TrackingFieldsMixin, SectionBasedModelMixin
)


class Quizz(TrackingFieldsMixin, SectionBasedModelMixin, models.Model):

    name = models.TextField(
        verbose_name=_("name")
    )

    weight = models.IntegerField(
        verbose_name=_("weight")
    )

    total_score = models.IntegerField(
        verbose_name=_("total score")
    )

    questions_count = models.IntegerField(
        verbose_name=_("questions count")
    )

    required = models.BooleanField(
        verbose_name=_("required")
    )

    options = models.JSONField(
        verbose_name=_("options")
    )

    class Meta:
        verbose_name = _("quizz")
        verbose_name_plural = _("quizzes")
