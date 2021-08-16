from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<str:pk>/', views.ProjectDetails.as_view()),
]