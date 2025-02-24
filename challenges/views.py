from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month) :
    monthList = list(month_by_key.keys()) #dict_keys(['a', 'b', 'c']), <class 'dict_keys'>
    if month > len(monthList):
        return HttpResponseNotFound("Invalid Month {}".format(month))
    
    current_month = monthList[month-1]
    return HttpResponseRedirect("/challenges/" + current_month)


def monthly_challenge(request, month) :
    try:
        challenge_text = month_by_key[month]
        response_data = f"<h1>{challenge_text}</h1>" #interpolated html
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Format Not supported for month</h1>")