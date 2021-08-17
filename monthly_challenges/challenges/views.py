from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

challengesDict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes a day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Eat no meat for the entire month",
    "may": "Walk for at least 20 minutes a day!",
    "june": "Learn Django for at least 20 minutes a day!",
    "july": "Eat no meat for the entire month",
    "august": "Walk for at least 20 minutes a day!",
    "september": "Learn Django for at least 20 minutes a day!",
    "october": "Eat no meat for the entire month",
    "november": "Walk for at least 20 minutes a day!",
    "december": "Learn Django for at least 20 minutes a day!",
}


def monthly_challenge_by_number(request, month: int):
    months = list(challengesDict.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
        
    redirect_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{redirect_month}")


def monthly_challenge(request, month: str):
    if month in challengesDict.keys():
        return HttpResponse(challengesDict[month])
    else:
        return HttpResponseNotFound("This month is not supported!")
