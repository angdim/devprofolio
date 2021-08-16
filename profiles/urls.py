from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfilesList.as_view()),
    path('profile/<str:pk>/', views.ProfileDetails.as_view()),
]