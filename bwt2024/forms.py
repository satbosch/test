# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""


from django.forms       import ModelForm
from .models            import *
#from django import forms
#from django.db.models import fields
#from django.views.generic.edit import UpdateView

###########################################################
# Object_Unit
###########################################################
class Object_Unit_Form(ModelForm):

    class Meta:
        model   = Object_Unit
        fields  = ['name','description']

