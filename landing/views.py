from django.shortcuts import render, get_object_or_404
from .models import Tournament
from django.contrib.auth.models import User
from team_interactions.models import Team
from users.models import UserProfile, TMProfile

# Create your views here.
def landing(request):
    tournaments = Tournament.objects.all()
    context = {
        'tournaments': tournaments
    }
    return render(request, "landing/main.html", context)


def show_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    return render(request, 'landing/tournament.html', {'tournament': tournament})


def calendar(request, year, month):
    tournaments = Tournament.objects.all()
    return render(request, "landing/calendar.html", {"tournaments": tournaments})


def rooster(request):
    tms = TMProfile.objects.all()
    return render(request, "landing/rooster.html", {"tms":tms})


def fp(request):
    return render(request, "landing/FairPlay.html", locals())


def tm_list(request):
    tournaments = Tournament.objects.all()
    context = {
        'tournaments': tournaments
    }
    return render(request, "landing/tournaments_list.html", context)

def team_list(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, "landing/teams_list.html", context)

def players_list(request):
    if request.user.is_authenticated:
        players = UserProfile.objects.exclude(user=request.user)
        owned_teams = Team.objects.filter(owner=request.user)
    else:
        players = UserProfile.objects.all()
        owned_teams = {}
    context = {
        'players': players, 'owned_teams' : owned_teams
    }
    return render(request, "landing/players_list.html", context)

def rating(request):
    return render(request, "landing/rating.html", locals())