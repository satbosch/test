# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.urls import path
from bwt2024.views          import *

urlpatterns = [

    path('home',                                        views_main.view_home,                         name='home'                   ),
    path('',                                            views_main.view_home,                         name='home'                   ),

    path('object_unit_list_edit',                       views_object_unit.object_unit_list_edit,      name='object_unit_list_edit'  ),
    path('object_unit_list',                            views_object_unit.object_unit_list,           name='object_unit_list'       ),
    path('object_unit_edit/<int:object_unit_id>/',      views_object_unit.object_unit_edit,           name='object_unit_edit'       ),
    path('object_unit_create',                          views_object_unit.object_unit_create,         name='object_unit_create'     ),

]