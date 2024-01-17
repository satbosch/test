# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

import os
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
from django.core.files.storage import FileSystemStorage

from mysite import settings

#####################################################################
# Upload file (redirect to function)
####################################################################
#@login_required(login_url="/login/")
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            project_name = form.cleaned_data['project_name']
            project_version = form.cleaned_data['project_version']
            file_name = uploaded_file.name

            if not file_name.endswith('.xml'):
                return JsonResponse({'success': False, 'error': 'Uploaded file is not an XML file'})

            response = upload_to_random_function(
                uploaded_file, project_name=project_name,
                project_version=project_version, file_name=file_name
            )

            if response.status_code == 200:
                messages.success(request, "File successfully uploaded")
            else:
                messages.error(request, f"An error occurred: {response.text}")

    else:
        form = UploadFileForm()

    return render(request, 'object_unit/object_upload.html', {'form': form})


#####################################################################
# Upload File Random Function
####################################################################
# Update this function to what you want the upload button to do when clicked

def upload_to_random_function(file_obj, uuid='', project_name='', project_version='', file_name='', auto_create=False):
 
    fs = FileSystemStorage(location=os.path.join(settings.UPLOADS_ROOT))
    filename = fs.save('FILE_' + str(file_name), file_obj)
    response = type('', (object,), {'status_code': 200})()  # Mock response with status_code 200

    return ResponseObject(response.status_code, response)


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
