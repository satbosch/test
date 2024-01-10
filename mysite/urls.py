# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.contrib import admin
from django.urls import include, path

# # remove on production
# from django.conf import settings
# from django.conf.urls.static import static
# # remove on production

urlpatterns = [
    path("admin/",      admin.site.urls),                   # Django admin route
    #path('api/', include('bwt2024.urls')),

    path("",            include("authentication.urls")),   # Auth routes - login
    path("",            include("bwt2024.urls")),
]


# # remove on production
# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# # remove on production