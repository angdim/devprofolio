# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
import uuid


# UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True,
    )
    email = models.EmailField(max_length=300, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
    )
    location = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    personal_info = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True,
        upload_to='staticfiles/', default='static/images/default-user-icon-33.jpg'
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    def __str__(self):
        return str(self.name)
