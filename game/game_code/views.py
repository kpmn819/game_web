from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Q

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
    total_games = Game.objects.count()

    right_5 = Game.objects.filter(score = 5).count()
    right_4 = Game.objects.filter(score = 4).count()
    unfinished = Game.objects.filter(score = -1).count()

    print('Total games are: '+ str(total_games))
    print('Perfect games= ' + str(right_5))
    print('4 out of 5 = ' + str(right_4))
    print('Unfinished games= ' + str(unfinished))

    # make dictionary
    turn_data = {'query_results': query_results}
    #print(turn_data)
    
    
    
    return render(request, 'game_code/home.html', turn_data)
