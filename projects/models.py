import uuid

from django.db import models


class ProjectModel(models.Model):
    title = models.CharField(
        max_length=200,
        default=None,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    source_code_link = models.URLField(
        # Allows registered users/developers to show project's source
        null=True,
        blank=True,
    )
    demo_link = models.URLField(
        # Allows registered users/developers to show working demo of their project
        null=True,
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
