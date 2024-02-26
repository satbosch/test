# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from rest_framework.response    import Response
from rest_framework             import status
from rest_framework             import permissions, viewsets
from rest_framework.views       import APIView
from bwt2024.serializers        import *

#####################################################################
# API - GET all - /api/Units/
####################################################################
class Object_Unit_ViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Object_Unit.objects.all()
    serializer_class = Object_Unit_Serializer
    lookup_field = "id"
    http_method_names = ['get', 'head', 'options']

#####################################################################
# API - Multi parameter GET request - /api/Units_Multi_Param/?name=a&description=a
####################################################################
class Object_Unit_Multi_Param_ViewSet(viewsets.ModelViewSet):
    serializer_class = Object_Unit_Serializer
    http_method_names = ['get', 'head', 'options']

    def get_queryset(self):
        queryset = Object_Unit.objects.all()
        name = self.request.query_params.get('name')
        description = self.request.query_params.get('description')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)

        return queryset

    