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
    #query_results = Game.objects.all()
    total_games = Game.objects.count()

    right_5 = Game.objects.filter(score = 5).count()
    right_4 = Game.objects.filter(score = 4).count()
    unfinished = Game.objects.filter(score = -1).count()
    
    wins_by_game=[]
    g_name = Game.objects.all().values_list('name', flat=True).distinct()
    for item in g_name:
        by_game_5 = Game.objects.filter(score = 5, name = item).count()
        by_game_5 = 'Perfect score in '+ item + '= '+ str(by_game_5)
        wins_by_game.append(by_game_5)
    
        print(wins_by_game)

        

    print('Total games are: '+ str(total_games))
    print('Perfect games= ' +  str(right_5))
    print('4 out of 5 = ' + str(right_4))
    print('Unfinished games= ' + str(unfinished))

    # make dictionary
    turn_data = {'wins_by_game': wins_by_game}
    print(turn_data)
    
    
    
    
    return render(request, 'game_code/home.html', turn_data)
