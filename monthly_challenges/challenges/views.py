"""challenges views"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge_by_number(request, month):
    """View for Challenges with number"""
    challenge_text = None
    if month == 1:
        challenge_text = 'january'
    elif month == 2:
        challenge_text = 'february'
    else:
        return HttpResponseNotFound()
    return HttpResponse(challenge_text)


def monthly_challenge(request, month):
    """View for Challenges with string"""
    challenge_text = None
    if month == 'january':
        challenge_text = 'january'
    elif month == 'february':
        challenge_text = 'february'
    else:
        return HttpResponseNotFound()

    return HttpResponse(challenge_text)
