from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    preview_image = models.ImageField(upload_to ='static/tournament_previews/', max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    THEME_CHOICES = (
        ('Высшая лига', 'Высшая лига'),
        ('Вторая лига', '2 лига'),
        ('Третья лига', '3 лига'),
    )
    creation_date = models.DateTimeField("",auto_now_add=True,blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    league = models.CharField(max_length=20, choices=THEME_CHOICES, unique=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    logo = models.ImageField(upload_to ='static/team_logo/', max_length=100)

    def __str__(self):
        return self.name