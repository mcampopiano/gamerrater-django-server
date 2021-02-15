from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    yearReleased = models.CharField(max_length=4)
    designer = models.CharField(max_length=10)
    numberOfPlayers = models.IntegerField()
    estDuration = models.CharField(max_length=10)
    ageRecommendation = models.IntegerField()
