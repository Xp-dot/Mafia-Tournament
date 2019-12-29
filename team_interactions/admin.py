from django.contrib import admin
from .models import Team, Contract

# Register your models here.
#admin.site.register(Photo, PhotoAdmin)

class ContractAdmin(admin.ModelAdmin):
    list_display=('player','team','duration','salary','contract_status')
    search_fields = ['player__username', 'team__name', 'contract_status',]


admin.site.register(Team)
admin.site.register(Contract,ContractAdmin)