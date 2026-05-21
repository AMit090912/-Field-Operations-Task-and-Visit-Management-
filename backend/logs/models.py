from django.db import models
from django.conf import settings


class ActivityLog(models.Model):

    ACTION_CHOICES = (
        ("TASK_CREATED", "Task Created"),
        ("VISIT_CREATED", "Visit Created"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=100,
        choices=ACTION_CHOICES
    )

    entity_type = models.CharField(max_length=100)

    entity_id = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action