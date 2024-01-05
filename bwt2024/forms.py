# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.views.generic.edit import UpdateView
from .models import *


###########################################################
# Object_Unit
###########################################################
class Object_Unit_Form(ModelForm):

    class Meta:
        model   = Object_Unit
        fields  = ['name','description']

