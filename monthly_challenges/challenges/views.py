"""challenges views"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge(request, month):
    """View for Challenges"""
    challenge_text = None
    if (month == 'january'):
        challenge_text = 'january'
    elif (month == 'february'):
        challenge_text = 'january'
    else:
        return HttpResponseNotFound

    return HttpResponse(challenge_text)
