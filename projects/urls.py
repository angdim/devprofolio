from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListCreate.as_view()),
]