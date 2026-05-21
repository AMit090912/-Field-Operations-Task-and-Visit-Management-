from django.db import models
from django.conf import settings

from tasks.models import Task


class Visit(models.Model):

    STATUS_CHOICES = (
        ("STARTED", "Started"),
        ("COMPLETED", "Completed"),
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )

    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="STARTED"
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    ai_summary = models.TextField(
        blank=True,
        null=True
    )

    risk_flag = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    started_at = models.DateTimeField(
        auto_now_add=True
    )

    completed_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Visit - {self.task.title}"