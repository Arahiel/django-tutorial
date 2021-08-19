from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
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

def index(request):
    ul = lambda input: f"<ul>\n{input}\n</ul>"
    li = lambda input: f"<li>{input}</li>"
    a = lambda name, link: f"<a href=\"{link}\">{name}</a>"
    abs_url = lambda relative_url: request.build_absolute_uri(relative_url)
    
    list_html = ul("\n".join([li(a(el, abs_url(reverse("month-challenge", args=[el])))) for el in list(challengesDict.keys())]))
    return HttpResponse(list_html)

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
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound("This month is not supported!")
