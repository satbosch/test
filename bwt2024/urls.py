from django.urls import path
from bwt2024.views          import *

urlpatterns = [

    path('home',            views_main.view_home,                    name='home'),
    path('',                views_main.view_home,                    name='home'),

]