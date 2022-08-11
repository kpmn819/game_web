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
    
    # easy to get all games
    total_games = Game.objects.count()
    # now how many with 4 or 5 right
    right_5 = Game.objects.filter(score = 5).count()
    right_4 = Game.objects.filter(score = 4).count()
    # how many were abandoned
    unfinished = Game.objects.filter(score = -1).count()
    
    # now for a challange, which answers were answered incorrect
    # most frequently first get all the incorrect questions
    result = Qna.objects.filter(correct = 0).values('question')
    # 
    most_wrong=[entry for entry in result]
    #print(most_wrong)
    list_wrong=[]
    for item in most_wrong:
        list_wrong.append(item['question'])
    # now get the unique list
    unique_questions=[]
    unique_set = set(list_wrong)
    # create a list of unique questions in the big list
    for item in unique_set:
        unique_questions.append(item)
    # now use this list to find out how many times it occures
    questions_occur=[]
    for item in unique_questions: 
        questions_occur.append((item, list_wrong.count(item)))
    # sort by value
    q_sort = sorted(questions_occur, key= lambda x: x[1], reverse= True)
    first_worst = q_sort[0][0] + ' was answered wrong ' + str(q_sort[0][1]) + ' times'
    second_worst = q_sort[1][0] + ' was answered wrong ' + str(q_sort[1][1]) + ' times'
    third_worst = q_sort[2][0] + ' was answered wrong ' + str(q_sort[2][1]) + ' times'
        

    print(q_sort)
    print(first_worst +'  '+ second_worst+'   '+third_worst)
    
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
    context = {'wins_by_game': wins_by_game, 'total_games': total_games, 'perfect_games':right_5, 'four_of_five':right_4,
                'unfinished':unfinished, 'first_worst':first_worst, 'second_worst':second_worst, 'third_worst':third_worst}
    
    
    
    
    return render(request, 'game_code/home.html', context)
