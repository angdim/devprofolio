import uuid

from django.db import models

from profiles.models import Profile


class Project(models.Model):
    owner = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
        default=None,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    project_image = models.ImageField(
        null=True, blank=True, upload_to='staticfiles/', default='static/images/default_project_image.jpg',
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
    approval = models.IntegerField(default=0, null=True, blank=True)  # Likes / total votes ratio
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

    class Meta:
        ordering = ['-approval', '-votes_count', 'title']

    @property
    def imageURL(self):
        try:
            url = self.project_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        likes = reviews.filter(value='like').count()
        total_votes = reviews.count()

        ratio = (likes / total_votes) * 100
        self.votes_count = total_votes
        self.approval = ratio

        self.save()


class Review(models.Model):
    VOTE_CHOICE = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
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

    class Meta:
        unique_together = [['owner', 'project']]

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
