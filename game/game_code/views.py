from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("Any text you want")

def v1(response):
    return HttpResponse("<h1>View 1</h1>")

def home(response):
    return render(response, 'game_code/home.html', {'somevar':'db stuff'})