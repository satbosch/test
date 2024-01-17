# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.urls        import path, include
from rest_framework     import routers
from bwt2024.views      import *


# remove on production
from django.conf import settings
from django.conf.urls.static import static
# remove on production

###########################################################
# API
###########################################################
router = routers.DefaultRouter()
router.register(r'Units', views_serializer.Object_Unit_ViewSet)

urlpatterns = [

    path('home',                                        views_main.view_home,                         name='home'                   ),
    path('',                                            views_main.view_home,                         name='home'                   ),

    ###########################################################
    # Object_Unit
    ###########################################################
    path('object_unit_list_edit',                       views_object_unit.object_unit_list_edit,      name='object_unit_list_edit'  ),
    path('object_unit_list',                            views_object_unit.object_unit_list,           name='object_unit_list'       ),
    path('object_unit_edit/<int:object_unit_id>/',      views_object_unit.object_unit_edit,           name='object_unit_edit'       ),
    path('object_unit_create',                          views_object_unit.object_unit_create,         name='object_unit_create'     ),

    ###########################################################
    # API
    ###########################################################
    path('api/', include(router.urls)),
    #path( 'ou/', views_serializer.Object_Unit_ViewSet.list),

    ###########################################################
    # Object_Upload
    ###########################################################
    path('object_upload',             views_object_upload.upload_file,         name='object_upload'),

    ###########################################################
    # Object_Download
    ###########################################################
    path('object_unit_download',             views_object_download.object_unit_download,         name='object_unit_download'),
]


# remove on production
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# remove on production