# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
import logging

logger = logging.getLogger(__file__)

###########################################################
# Login
###########################################################
def view_login(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info("Login: " + username)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'
                logger.info("Invalid credentials: " + username)
        else:
            msg = 'Error validating the form'    

    return render(request, "login.html", {"form": form, "msg" : msg})

###########################################################
# logout
###########################################################
def view_logout(request):
    logout(request)
    return redirect('home')