from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField("01-01-1993", blank=True)
    end_date = models.DateTimeField("01-01-1993", blank=True)
    preview_image = models.ImageField(upload_to ='static/tournament_previews/', max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    logo = models.ImageField(upload_to ='static/team_logo/', max_length=100)

    def __str__(self):
        return self.name