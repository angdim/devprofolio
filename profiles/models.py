from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # email =
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
        upload_to='profiles/', default='profiles/default-user-icon-33.jpg'
    )
    created = models.DateTimeField(auto_now_add=True)

