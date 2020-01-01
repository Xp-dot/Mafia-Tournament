from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

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
    status_choices = ((1, 'Рассматривается игроком'), (2, 'Рассматривается владельцем'), (3, "Принят"), (4, "Отклонен"), (5, "Запрос на расторжение владельцем"),
                      (6, "Запрос на расторжение игроком"), (7, 'Расторгнут'))
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

    def get_income_transitions(self):
        if self.contract_status == 1:
            return [(4,'Отклонить')]
        elif self.contract_status == 2:
            return [(3,'Принять'), (4,'Отклонить')]
        elif self.contract_status == 3:
            return [(5,'Расторгнуть(влд)')]

    def get_outcome_transitions(self):
        if self.contract_status == 1:
            return [(3,'Принять'), (4,'Отклонить')]
        elif self.contract_status == 2:
            return [(4,'Отклонить')]
        elif self.contract_status == 3:
            return [(6,'Расторгнуть(игр)')]

    @staticmethod
    def post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        if instance.contract_status == 7:
            instance.player.userprofile.revoke_contract()

post_save.connect(Contract.post_save, sender=Contract)