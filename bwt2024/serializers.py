# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from rest_framework     import serializers
from bwt2024.models     import *

class Object_Unit_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object_Unit
        fields = ['id','name','description']
