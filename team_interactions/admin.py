from django.contrib import admin
from .models import Team, Contract

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display=('name','league','owner','creation_date', 'can_play', 'active_players')
    search_fields = ['name', 'league', 'owner__username','creation_date','active_players']


class ContractAdmin(admin.ModelAdmin):
    list_display=('player','team','duration','salary','contract_status')
    search_fields = ['player__username', 'team__name', 'contract_status',]


admin.site.register(Team, TeamAdmin)
admin.site.register(Contract,ContractAdmin)