from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey

class Rating(models.Model):
    player = ForeignKey("Player", on_delete=models.CASCADE)
    game = ForeignKey("Game", on_delete=models.CASCADE)
    rating = IntegerField()