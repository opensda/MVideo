from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("mvideo.urls", namespace='mvideo')),
    path("users/", include("users.urls", namespace="users")),
]
