from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/",      admin.site.urls),                   # Django admin route

    path("",            include("authentication.urls")),   # Auth routes - login
    path("",            include("bwt2024.urls")),
]