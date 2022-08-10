
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    dtime =models.CharField(max_length=200)
    score = models.IntegerField()
    free = models.BooleanField()



    def __str__(self):
        return self.name

class Qna(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    q_number = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField()
    def __str__(self):
        return self.name
    