from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=256)
    color_in_calendar = models.CharField(max_length=8)
    description = models.TextField()
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    preview_image = models.ImageField(upload_to ='static/tournament_previews/', max_length=100)

    def __str__(self):
        return self.name