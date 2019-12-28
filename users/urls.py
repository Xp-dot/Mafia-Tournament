from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('teams_management/', views.team_management, name='team_management'),
    path('my_contracts/', views.my_contracts, name='my_contracts'),
    path('my_team/', views.my_team, name='my_team'),
]