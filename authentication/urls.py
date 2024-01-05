# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.urls import path
from authentication.views          import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/',          view_login,        name="login"),
    path("logout/",         view_logout,       name="logout")

]
