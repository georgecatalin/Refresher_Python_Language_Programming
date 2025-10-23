from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello this is my first Django page")


def february_function(request):
    return HttpResponse("Hello from february")