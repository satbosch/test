# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.fields import CommaSeparatedIntegerField
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from bwt2024.forms import *
from bwt2024.models import *
from django.forms import *


###########################################################
# Object_Unit
###########################################################
@login_required(login_url="/login/")
def object_unit_list(request):
    context = {}

    try:

        Object_Unit_FormSet = modelformset_factory(Object_Unit, form=Object_Unit_Form, can_delete=True, fields = ('name','description') )
        context['formset'] = Object_Unit_FormSet(queryset=Object_Unit.objects.all())

        if request.method=='POST' and 'btn_list_edit_save' in request.POST:
            formset = Object_Unit_FormSet(request.POST)
            if formset.is_valid():
                instances = formset.save(commit=False)
                for instance in instances:
                    try:
                        instance.save()
                        messages.success(request, 'Object Unit ' + instance.name + ' saved sucessfully.' )
                    except:
                        messages.error(request, 'Object Unit ' + instance.name + ' not saved.' )
                for obj in formset.deleted_objects:
                    try:
                        messages.success(request, 'Object Unit ' + obj.name + ' deleted sucessfully.' )
                        obj.delete()
                    except:
                        messages.error(request, 'Object Unit ' + obj.name + ' not deleted.' )
            else:
                messages.error(request, 'Error: Object Unit Form was not saved.' )
                for error in formset.errors:
                    messages.error(request, str(error) )

        load_template           = "object_unit\list_edit.html"
        context['segment']      = load_template
        context['PageTitle']    = "Object Units "
        context['msghelp']      = "This is an Help message"
        context['breadcrumbs']  = [{'Name' : 'Home', 'Link' : '/', 'Active': False} , {'Name' : 'Object Units', 'Link' : '/Object_unit_form', 'Active': True}]

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'errors/page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template( 'errors/page-500.html' )
        return HttpResponse(html_template.render(context, request))

