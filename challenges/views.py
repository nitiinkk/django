from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string

# Create your views here.
month_by_key = {
    "january": "Walk for 10 mins",
    "february": "eat for 10 mins",
    "march": "sleep for 10 mins",
    "april": "dance for 10 mins",
    "may": "sing for 10 mins",
    "june": "jump for 10 mins",
    "july": "run for 10 mins",
    "august": "bing watch for 10 mins",
    "september": "shout for 10 mins",
    "october": "yoga for 10 mins",
    "november": "exercise for 10 mins",
    "december": "drive for 10 mins"
}

def index(request) :
    list_items = ""
    months = list(month_by_key.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items+=f"<h1><a href=\"{month_path}\">{capitalized_month}</a></h1>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month) :
    monthList = list(month_by_key.keys()) #dict_keys(['a', 'b', 'c']), <class 'dict_keys'>
    if month > len(monthList):
        return HttpResponseNotFound("Invalid Month {}".format(month))
    
    current_month = monthList[month-1]
    return HttpResponseRedirect("/challenges/" + current_month)


def monthly_challenge(request, month) :
    try:
        challenge_text = month_by_key[month]
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "current_month": month
        })
    except:
        return HttpResponseNotFound("<h1>Format Not supported for month</h1>")