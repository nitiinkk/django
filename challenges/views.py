from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge_by_number(request, month) :
    return HttpResponse(month)

def monthly_challenge(request, month) :
    challenge_text = None
    if month == "january":
        challenge_text = "Walk for 10 mins"
    elif month == "february":
        challenge_text = "take rest for 10 mins"
    else:
        return HttpResponseNotFound(" Format Not supported for month: {}".format(month))
                                    
    return HttpResponse(challenge_text)