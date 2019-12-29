from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    league_CHOICES = (
        (1, 'Высшая лига'),
        (2, 'Вторая лига'),
        (3, 'Третья лига'),
    )
    creation_date = models.DateTimeField("",auto_now_add=True,blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    league = models.PositiveSmallIntegerField(choices=league_CHOICES, default=3)
    name = models.CharField(max_length=256)
    description = models.TextField()
    logo = models.ImageField(upload_to ='static/team_logo/', max_length=100)

    def __str__(self):
        return self.name

class Contract(models.Model):
    status_choices = ((1, 'Рассматривается'), (2, "Принят"), (3, "Отклонен"), (4, "Изменен"), (5, "Расторгнут"))
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_player')
    team_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_team_owner')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    duration = models.IntegerField(default=2)
    salary = models.IntegerField(default=0)
    contract_value = models.IntegerField(default=0)
    contract_status = models.PositiveSmallIntegerField(choices=status_choices, default=1)

    def __str__(self):
        return self.player.username

    def change_status(self, new_status):
        self.contract_status = new_status
        self.save()
        pass