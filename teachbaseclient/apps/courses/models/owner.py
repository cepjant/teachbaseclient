from django.db import models
from django.utils.translation import gettext_lazy as _


class Owner(models.Model):
    """ Модель владельца курса """

    name = models.TextField(
        verbose_name=_("name"),
    )

    class Meta:
        verbose_name = _("course owner")
        verbose_name_plural = _("course owners")
