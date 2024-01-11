# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

import time
import base64
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib                     import messages
from django.contrib.auth.decorators     import login_required
from bwt2024.forms                      import *
from bwt2024.models                     import *
from django.forms                       import *

# Environmental Variables
BWT_API_URL="https://bwt.bosch.com"
API_KEY_BWT="API KEY HERE"
#####################################################################
# Upload file (redirect to function)
####################################################################
#@login_required(login_url="/login/")
def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        # Change parameters according to your form
        if form.is_valid():
            uploaded_file = request.FILES['file']
            project_name = form.cleaned_data['project_name']
            project_version = form.cleaned_data['project_version']
            file_name = uploaded_file.name

            # Check if the file ends with .xml or, for any other extension, change the following parameter
            if not file_name.endswith('.xml'):
                return JsonResponse({'success': False, 'error': 'Uploaded file is not an XML file'})
            
            # Parameters can be personalized, this is just an example
            response = upload_to_random_function(
                uploaded_file, project_name=project_name,
                project_version=project_version
            )

            if response.status_code == 200:
                messages.success(request, "File successfully uploaded")
                return redirect('home')

            else:
                messages.error(request, f"An error occurred: {response.text}")



    else:
        form = UploadFileForm()

    return render(request, 'object_unit/object_upload.html', {'form': form})

#####################################################################
# Upload File Random Function
####################################################################
# Update this function to what you want the upload button to do when clicked

def upload_to_random_function(file_obj, uuid='', project_name='', project_version='', auto_create=False):
    BWT_URL = BWT_API_URL+"/api/v1/bom" 
    BWT_HEADERS = {
        "Content-Type": "application/json"
    }

    # Read the file content and encode it to base64 (needed to upload it to api)
    bom_content = base64.b64encode(file_obj.read()).decode('utf-8')

    # transversal data for both scenarios
    data = {
        'bom': bom_content
    }
    try:
        response = requests.put(BWT_URL, headers=BWT_HEADERS, json=data)
        return ResponseObject(response.status_code, response.text)
    except requests.RequestException as e:
        return ErrorResponse(500, str(e))

#####################################################################
# Error Handling
####################################################################
class ErrorResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

class ResponseObject:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text
