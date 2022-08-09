import imp
from django.shortcuts import render
from django.http import HttpResponse
from .models import Game
from .models import Qna

# Create your views here.
def index(response):
    return HttpResponse("Any text you want")

def v1(response):
    return HttpResponse("<h1>View 1</h1>")

def home(request, id):
    game_data = Game.objects.get(id=id)
    #turn_data = Qna.objects.get(id=id)
    return render(request, 'game_code/home.html', {'game_data':game_data})