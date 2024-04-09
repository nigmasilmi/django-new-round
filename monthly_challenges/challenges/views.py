"""challenges views"""
from django.shortcuts import render
from django.urls import reverse
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


def index(request):
    """index view"""
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('name-month-challenge', args=[month])
        list_items += f'<li><a href=\"{month_path}\">{capitalized_month}</a></li>'
        response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    """View for Challenges with number"""
    monthly_keys = list(monthly_challenges.keys())
    if month > len(monthly_keys):
        return HttpResponseNotFound('Sorry, this month went on vacations')
    target_month = monthly_keys[month - 1]
    # challenge/, month string => /challenge/january
    reversed_path = reverse('name-month-challenge', args=[target_month])
    return HttpResponseRedirect(reversed_path)


def monthly_challenge(request, month):
    """View for Challenges with string"""
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"challenge_text": challenge_text, "month": month})
    except KeyError:
        return HttpResponseNotFound('sorry, this challenge is not available')
