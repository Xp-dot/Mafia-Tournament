from django.db import models
from django.contrib.auth.models import User
from team_interactions.models import Team
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leagues = ((1, "Имеет допуск к высшей лиге"), (2, "Имеет допуск ко второй лиге"), (3, "Имеет допуск к третьей лиге"))
    access = models.PositiveSmallIntegerField(choices=leagues, default=3)
    in_team = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True )
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
