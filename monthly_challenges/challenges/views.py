"""challenges views"""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """View for index"""
    return HttpResponse("Hello world!")
