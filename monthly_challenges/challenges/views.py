"""challenges views"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    'january': 'lorem ipsum january',
    'february': 'lorem ipsum february',
    'march': 'lorem ipsum march',
    'april': 'lorem ipsum april',
    'may': 'lorem ipsum may',
    'june': 'lorem ipsum june',
    'july': 'lorem ipsum july',
    'august': 'lorem ipsum august',
    'september': 'lorem ipsum september',
    'october': 'lorem ipsum october',
    'november': 'lorem ipsum november',
    'december': 'lorem ipsum december',
}


def monthly_challenge_by_number(request, month):
    """View for Challenges with number"""
    monthly_keys = list(monthly_challenges.keys())
    target_month = monthly_keys[month - 1]
    return HttpResponseRedirect("/challenges/" + target_month)


def monthly_challenge(request, month):
    """View for Challenges with string"""
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
    except KeyError:
        return HttpResponseNotFound('sorry, this challenge is not available')

    return HttpResponse(challenge_text)
