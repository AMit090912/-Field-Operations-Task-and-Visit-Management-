from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("REGIONAL_MANAGER", "Regional Manager"),
        ("TEAM_LEAD", "Team Lead"),
        ("FIELD_AGENT", "Field Agent"),
        ("AUDITOR", "Auditor"),
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default="FIELD_AGENT"
    )

    region = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    team = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )