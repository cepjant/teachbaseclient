from django.db import models
from django.utils.translation import gettext_lazy as _


class TrackingFieldsMixin(models.Model):
    """Миксин с полями для отслеживания создания
    и изменения объекта"""

    created_at = models.DateTimeField(verbose_name=_("created at"))

    updated_at = models.DateTimeField(verbose_name=_("updated at"))

    class Meta:
        abstract = True


class SectionBasedModelMixin(models.Model):
    """Миксин для моделей, зависящих (имеющих FK поле)
    от модели Section"""

    section = models.ForeignKey(
        verbose_name=_("section"), to="Section", on_delete=models.CASCADE
    )

    position = models.IntegerField(verbose_name=_("position"))

    section_position = models.IntegerField(verbose_name=_("section position"))

    class Meta:
        abstract = True
