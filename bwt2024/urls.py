from django.urls import path

from . import views

urlpatterns = [


    path('home',            views.index,                    name='home'),
    path('',                views.index,                    name='home'),

    path('logout',            views.index,                    name='logout'),

    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:unit_name>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:unit_name>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:unit_name>/vote/", views.vote, name="vote"),
]