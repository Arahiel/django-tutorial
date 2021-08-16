from django.http import HttpResponse
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
# Create your views here.

challengesDict = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes a day!",
    "march": "Learn Django for at least 20 minutes a day!",
    "april": "Eat no meat for the entire month",
    "may": "Eat no meat for the entire month",
    "june": "Eat no meat for the entire month",
    "july": "Eat no meat for the entire month",
    "august": "Eat no meat for the entire month",
    "september": "Eat no meat for the entire month",
    "october": "Eat no meat for the entire month",
    "november": "Eat no meat for the entire month",
    "december": "Eat no meat for the entire month",
}

def monthly_challenge(request, month):
    if month in challengesDict.keys():
        return HttpResponse(challengesDict[month])
    else:
        return HttpResponseNotFound("This month is not supported!")