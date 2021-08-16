from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfilesList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
