from django.shortcuts import render

from django.http import HttpResponse


def index2(request):
    return HttpResponse("Hello, world. You're at the Bosch Web Template 2024 index.")


def index(request):
    context = {}
    context['texto'] = "Hello, world. You're at the Bosch Web Template 2024."
    return render(request, "unit/unit.html", context)


def detail(request, unit_name):
    return HttpResponse("You're looking at question %s." % unit_name)


def results(request, unit_name):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % unit_name)


def vote(request, unit_name):
    return HttpResponse("You're voting on question %s." % unit_name)