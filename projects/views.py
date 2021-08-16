from rest_framework import status, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from projects.models import Project
from projects.restrictions import IsFullAdmin
from projects.serializers import ProjectSerializer


class ProjectList(ListAPIView):
    # permission_classes=(permissions.AllowAny)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    queryset = Project.objects.get_queryset()
    serializer_class = ProjectSerializer
