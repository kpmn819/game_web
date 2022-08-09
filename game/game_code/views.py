from django.shortcuts import render
from django.http import HttpResponse

#from game import game
from .models import Game, Qna

# Create your views here.
def index(response, id):
    game_data = Game.objects.get(id=id)
    return HttpResponse('<h1>%s</h1>' % game_data.name)

def v1(response):
    return HttpResponse("<h1>View 1</h1>")

def home(request):
    #turn_data = Qna.objects.get(all)
    #turn_data = [{'question':'specs', 'answer':'33'}, {'question':'shoes','answer':'99'}]
    
    # get everything
    query_results = Game.objects.all()
    # make dictionary
    turn_data = {'query_results': query_results}
    print(turn_data)
    
    
    
    return render(request, 'game_code/home.html', turn_data)
