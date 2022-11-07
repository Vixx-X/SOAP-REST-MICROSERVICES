"""
Models for saving Submissions
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Submission(models.Model):

    input = models.TextField(
        _("Input"),
    )

    output = models.TextField(
        _("Output"),
        null=True,
    )

    date_updated = models.DateTimeField(
        _("Date updated"),
        auto_now=True,
        db_index=True,
    )

    date_created = models.DateTimeField(
        _("Date created"),
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        app_label = "soap"
        db_table = "submissions"
        verbose_name = _("Submission")
        verbose_name_plural = _("Submissions")

    def __str__(self):
        return f"Submission #{self.id} - {self.date_created}"
