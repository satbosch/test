from django.urls import path
from bwt2024.views          import *

from . import views

urlpatterns = [

    path('home',            views_main.home,                    name='home'),
    path('',                views_main.home,                    name='home'),

    #path('logout',            views.home,                    name='logout'),

]