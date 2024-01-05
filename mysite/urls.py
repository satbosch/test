from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("bwt2024/", include("bwt2024.urls")),
    path("admin/", admin.site.urls),
]