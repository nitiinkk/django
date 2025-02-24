from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse("Reduce screen time by 10 minutes")

def february(request):
    return HttpResponse("Go for daily walk for 20 minutes")