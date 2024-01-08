# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from rest_framework.response    import Response
from rest_framework             import status
from rest_framework             import permissions, viewsets
from rest_framework.views       import APIView
from bwt2024.serializers        import *

class Object_Unit_ViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Object_Unit.objects.all()
    serializer_class = Object_Unit_Serializer
    lookup_field = "id"


#class Object_Unit_View(APIView):
#    def get(self, request):
#            Object_Units = Object_Unit.objects.all()
#            return Response({"ous": Object_Units})


#    # 1. List all
#    def get(self, request, *args, **kwargs):
#        """
#        API endpoint that allows Object_Unit to be viewed
#        """
#        queryset = Object_Unit.objects.all()
#        serializer_class = Object_Unit_Serializer
#        return Response(serializer_class.data, status=status.HTTP_200_OK)


    