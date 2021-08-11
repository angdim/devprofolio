from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('profiles/', include('profiles.urls')),
    path('', include('auth_devs.urls')),
]
