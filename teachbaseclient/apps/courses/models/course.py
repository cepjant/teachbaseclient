from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from teachbaseclient.apps.courses.models.mixins import TrackingFieldsMixin


class Course(TrackingFieldsMixin, models.Model):
    """Модель курса"""

    name = models.TextField(
        verbose_name=_("name"),
    )

    content_type = models.PositiveIntegerField(
        verbose_name=_("content type"),
    )

    owner = models.ForeignKey(
        verbose_name=_("owner"), to="Owner", on_delete=models.SET_NULL, null=True
    )

    thumb_url = models.TextField(
        verbose_name=_("thumb url"),
    )

    cover_url = models.TextField(
        verbose_name=_("cover url"),
    )

    description = models.TextField(
        verbose_name=_("description"),
    )

    last_activity = models.DateTimeField(
        verbose_name=_("last activity"),
    )

    total_score = models.PositiveIntegerField(
        verbose_name=_("total score"),
    )

    total_tasks = models.PositiveIntegerField(
        verbose_name=_("total tasks"),
    )

    is_netology = models.BooleanField(
        verbose_name=_("netology"),
    )

    bg_url = models.TextField(
        verbose_name=_("bg url"),
    )

    video_url = models.TextField(
        verbose_name=_("video url"),
    )

    demo = models.BooleanField(
        verbose_name=_("demo"),
    )

    unchangeable = models.BooleanField(
        verbose_name=_("unchangeable"),
    )

    include_weekly_report = models.BooleanField(
        verbose_name=_("include weekly report"),
    )

    custom_author_names = models.TextField(
        verbose_name=_("custom author names"),
    )

    custom_contents_link = models.TextField(
        verbose_name=_("custom contents link"),
    )

    hide_viewer_navigation = models.BooleanField(
        verbose_name=_("hide viewer navigation"),
    )

    duration = models.PositiveIntegerField(
        verbose_name=_("duration"),
    )

    authors = models.ManyToManyField(
        to="Author",
        verbose_name=_("authors"),
    )

    types = models.ManyToManyField(
        to="CourseType",
        verbose_name=_("types"),
    )

    competences = ArrayField(
        verbose_name=_("competences"), base_field=models.TextField()
    )

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")
