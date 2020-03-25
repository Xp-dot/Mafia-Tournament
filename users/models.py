from django.db import models
from django.contrib.auth.models import User,Group
from team_interactions.models import Team, Contract
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leagues = ((1, "Имеет допуск к высшей лиге"), (2, "Имеет допуск ко второй лиге"), (3, "Имеет допуск к третьей лиге"))
    access = models.PositiveSmallIntegerField(choices=leagues, default=3)
    in_team = models.BooleanField(default=False)
    in_reserve = models.BooleanField(default=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True )
    def __str__(self):
        return self.user.username

    def change_reserve_state(self):
        self.in_reserve = not self.in_reserve
        if self.in_reserve:
            self.team.change_active(-1)
        else:
            self.team.change_active(+1)
        self.save()

    def signup_contract(self, contract):
        self.in_team = True
        self.team = contract.team
        self.save()

    def revoke_contract(self):
        print('contract was revoked for player ' + str(self.user.username))
        self.in_team = False
        self.team = None
        self.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class TMProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    cup_list = ((1, "Золотой кубок"), (2, "Серебряный кубок"), (3, "Нет кубка"))
    cups = models.PositiveSmallIntegerField(choices=cup_list, default=3)
    access_to_admin = models.BooleanField(default=True)
    status = models.CharField(max_length=256, default='Turnir master')
    comment = models.CharField(max_length=256, default='pidor')
    def __str__(self):
        return self.user.username

@receiver(post_save, sender = TMProfile)
def create_TM_user_profile(sender, instance, created, **kwargs):
    if created:
        group = instance.group
        instance.user.groups.add(group)
        instance.user.is_staff=instance.access_to_admin
        instance.user.save()

@receiver(post_delete, sender = TMProfile)
def create_TM_user_profile(sender, instance, **kwargs):
    group = instance.group
    instance.user.groups.clear()
    instance.user.is_staff=False
    instance.user.save()