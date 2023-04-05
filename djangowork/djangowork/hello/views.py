from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def sajjad(request):
    return HttpResponse("Hello, Sajjad!")

def shah(request):
    return HttpResponse("Selam, Shah Gi!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
