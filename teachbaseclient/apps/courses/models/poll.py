from django.db import models
from django.utils.translation import gettext_lazy as _


class Poll(models.Model):

    name = models.TextField(
        verbose_name=_("name")
    )

    required = models.BooleanField(
        verbose_name=_("required")
    )

    introduction = models.TextField(
        verbose_name=_("introduction")
    )

    final_message = models.TextField(
        verbose_name=_("final message")
    )

    section_position = models.IntegerField(
        verbose_name=_("section position")
    )

    class Meta:
        verbose_name = _("poll")
        verbose_name_plural = _("polls")
