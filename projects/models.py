import uuid

from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=200,
        default=None,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    source_code_link = models.URLField(
        # Allows registered profiles/developers to show project's source
        null=True,
        blank=True,
    )
    demo_link = models.URLField(
        # Allows registered profiles/developers to show working demo of their project
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField('Tag', blank=True)
    votes_count = models.IntegerField(default=0, null=True, blank=True)
    approval = models.IntegerField(default=0, null=True, blank=True) # Likes / total votes ratio
    created = models.DateTimeField(
        auto_now_add=True,
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_CHOICE = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(
        null=True,
        blank=True,
    )
    vote = models.CharField(
        max_length=200,
        choices=VOTE_CHOICE,
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

    def __str__(self):
        return self.vote


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(
        auto_now_add=True,
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.name
