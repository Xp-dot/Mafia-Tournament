"""Mafia_Tournaments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('tm_calendar/<int:year>/<int:month>', views.calendar, name="tm_calendar"),
    path("tm_FP", views.fp, name="tm_FP"),
    path("tm_roster", views.rooster, name="tm_roster"),
    path("tm_tournaments_list", views.tm_list, name="tm_tournaments_list"),
    path("tm_teams", views.team_list, name="tm_teams"),
    path("tm_rating", views.rating, name="tm_rating"),
    path('tournament/<tournament_id>', views.show_tournament, name='tournament')
]
