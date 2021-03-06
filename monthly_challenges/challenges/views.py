from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
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
    "december": None
}


def index(request):
    return render(request, "challenges/index.html", {
        "month_list": list(challengesDict.keys())
    })


def monthly_challenge_by_number(request, month: int):
    months = list(challengesDict.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month: str):
    if month in challengesDict.keys():
        challenge_text = challengesDict[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    else:
        raise Http404()
