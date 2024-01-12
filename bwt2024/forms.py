# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""


from django.forms       import ModelForm
from .models            import *
from django import forms
#from django.db.models import fields
#from django.views.generic.edit import UpdateView

###########################################################
# Object_Unit - Lista/Edit
###########################################################
class Object_Unit_Form(ModelForm):

    class Meta:
        model   = Object_Unit
        fields  = ['name','description']

###########################################################
# Object_Unit - Lista
###########################################################
class Object_Unit_Create_Form(ModelForm):

    class Meta:
        model   = Object_Unit_Create
        fields = ['name', 'version', 'homepage', 'mitre_name', 'mitre_version', 'vendor', 'cpe']
###########################################################
# Upload File
###########################################################
class UploadFileForm(forms.Form):
    file = forms.FileField()
    project_name = forms.CharField(required=False, label="Project Name", max_length=200,         widget=forms.TextInput(attrs={'style': 'width:100%;', 'placeholder': 'Enter project name if UUID is not available'}))
    project_version = forms.CharField(required=False, label="Project Version", max_length=50,         widget=forms.TextInput(attrs={'style': 'width:100%;', 'placeholder': 'Enter project version if UUID is not available'}))
