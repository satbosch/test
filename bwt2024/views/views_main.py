# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

import logging
from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from bwt2024.models import *


from django.db import connection

logger = logging.getLogger(__file__)

###########################################################
# home 
###########################################################
#@login_required(login_url="/login/")
def view_home(request):
    context = {}

    # try:

        #init_db()
        
    load_template           = "home.html"
    context['segment']      = load_template
    context['PageTitle']    = "Home"
    context['msghelp']      = "bwt2024 <br\>" \
                            + "XC/EVI <br><br>" \
                            + "Help message"
    context['breadcrumbs']  = [{'Name' : 'Home', 'Link' : '/', 'Active': True}]

    #logger.debug("This logs a debug message.")
    #logger.info("This logs an info message.")
    #logger.warn("This logs a warning message.")
    #logger.error("This logs an error message.")

    context['VulnerableComponents'] = 0
    context['VulnerabilityScans']   = 0

        #cursor = connection.cursor()
        #try:
        #    storedProc          = '''EXEC [dbo].[0000_SSP_Dashboard]'''
        #    cursor.execute(storedProc)
        #    result_set          = cursor.fetchall()
        #finally:
        #    cursor.close()

        #    context['Customers']                = result_set[0][0]
        #    context['Projects']                 = result_set[0][1]
        #    context['VulnerableComponents']     = result_set[0][2]
        #    context['VulnerabilityScans']       = result_set[0][3]
    
    html_template = loader.get_template( load_template )
    return HttpResponse(html_template.render(context, request))

    # except template.TemplateDoesNotExist as e:
    #     logging.getLogger("error_logger").error(repr(e))
    #     html_template = loader.get_template( 'errors/page-404.html' )
    #     return HttpResponse(html_template.render(context, request))

    # except Exception as e:
    #     logging.getLogger("error_logger").error(repr(e))
    #     logger.exception("This logs an exception.")
    #     html_template = loader.get_template( 'errors/page-500.html' )
    #     return HttpResponse(html_template.render(context, request))
