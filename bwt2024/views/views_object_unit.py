# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django                             import template
from django.contrib                     import messages
from django.contrib.auth.decorators     import login_required, permission_required
#from django.db.models.fields import CommaSeparatedIntegerField
from django.http                        import HttpResponse
from django.shortcuts                   import get_object_or_404, redirect, render
from django.template                    import loader
from bwt2024.forms                      import *
from bwt2024.models                     import *
from django.forms                       import *


###########################################################
# Object_Unit List/Edit
###########################################################
@login_required(login_url="/login/")
def object_unit_list_edit(request):
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

        load_template           = "object_unit\object_unit_list_edit.html"
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

###########################################################
# Object_Unit Create
###########################################################
@login_required(login_url="/login/")
def object_unit_create(request):
    context = {}

    try:

        if request.method == 'POST':
            form = Object_Unit_Create_Form(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Object Unit created successfully.')
                return redirect('object_unit_list')
            else:
                messages.error(request, 'Error: Form is not valid. Please check your input.')
        else:
            form = Object_Unit_Create_Form()

        return render(request, 'object_unit/object_unit_create.html', {'form': form})
        
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'errors/page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template( 'errors/page-500.html' )
        return HttpResponse(html_template.render(context, request))

###########################################################
# BOMDictionary Edit
###########################################################
@login_required(login_url="/login/")
def object_unit_edit(request,object_unit_id):
    context = {}

    try:

        object_unit = Object_Unit.objects.get(pk=object_unit_id)
        context['object_unit'] = object_unit

        if request.method == 'POST' and 'btn_object_unit_cancel' in request.POST:
            return redirect('object_unit_list')

        elif request.method == 'POST' and 'btn_object_unit_save' in request.POST:
            form = Object_Unit_Form(request.POST, instance = object_unit)
            if form.is_valid():
                form.save()
                messages.success(request, 'BOM Dictionary Entry '+ str(object_unit.cpe) + ' saved.')
                return redirect('object_unit_list')

        load_template           = "object_unit/object_unit_edit.html"
        context['segment']      = load_template
        context['PageTitle']    = "BOM Dictionary Edit"
        context['msghelp']      = "This is an Help message"
        context['msghelp']      = "This is an Help message"
        context['breadcrumbs']  = [{'Name' : 'Home', 'Link' : '/', 'Active': False} , {'Name' : 'BOM Dictionary List', 'Link' : '/object_unit_list', 'Active': False}, {'Name' : 'BOM Dictionary Edit', 'Link' : '', 'Active': True}]
        
        form = Object_Unit_Form(instance=object_unit)
        context['form'] = form

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'errors/page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template( 'errors/page-500.html' )
        return HttpResponse(html_template.render(context, request))

###########################################################
# BOMDictionary List
###########################################################
@login_required(login_url="/login/")
def object_unit_list(request):
    context = {}

    try:

        if request.method=='POST' and 'btn_object_unit_edit' in request.POST:
            object_unit_id = request.POST.get('btn_object_unit_edit')
            return redirect('object_unit_edit', object_unit_id)

        elif request.method=='POST' and 'btn_object_unit_create' in request.POST:
            return redirect('object_unit_create')

        load_template           = "object_unit/object_unit_list.html"
        context['segment']      = load_template
        context['PageTitle']    = "BOM Dict List"
        context['msghelp']      = "This is an Help message"
        context['breadcrumbs']  = [{'Name' : 'Home', 'Link' : '/', 'Active': False} , {'Name' : 'BOM Dictionary List', 'Link' : '/object_unit_list', 'Active': True}]

        context['object_unit_list'] = Object_Unit_Create.objects.all()
        load_template = "object_unit/object_unit_list.html"
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'errors/page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template( 'errors/page-500.html' )
        return HttpResponse(html_template.render(context, request))
