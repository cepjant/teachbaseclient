from django.db import models
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models import (
    Course, Poll
)


class Section(models.Model):
    """ Модель секций курса """

    course = models.ForeignKey(
        verbose_name=_("course"),
        to=Course,
        on_delete=models.CASCADE
    )

    name = models.TextField(
        verbose_name=_("name")
    )

    draft = models.BooleanField(
        verbose_name=_("draft")
    )

    icon_url = models.TextField(
        verbose_name=_("icon url")
    )

    small_url = models.TextField(
        verbose_name=_("small url")
    )

    thumb_url = models.TextField(
        verbose_name=_("thumb url")
    )

    icon_content_type = models.TextField(
        verbose_name=_("icon content type")
    )

    polls = models.ManyToManyField(
        verbose_name=_("polls"),
        to=Poll
    )

    class Meta:
        verbose_name = _("course section")
        verbose_name_plural = _("course sections")
