from django.contrib import admin
from .models import *

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','access','in_team','in_reserve', 'team')
    search_fields = ['user__username', 'access', 'in_team','in_reserve','team__name']

class TMProfileAdmin(admin.ModelAdmin):
    list_display=('user','cups','status','comment')
    search_fields = ['user__username', 'cups', 'status',]


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(TMProfile,TMProfileAdmin)