from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge(request,month):
    challenge_text = None
    if month == "january":
        challenge_text = "This is January challenge"
    elif month == "february":
        challenge_text = "This is February challenge"
    elif month == "march":
        challenge_text = "This is March challenge"
    else:
        return HttpResponseNotFound("This page does not exist on the server")
    return HttpResponse(challenge_text)

def monthly_challenge_int(request, month):
    return HttpResponse(month)