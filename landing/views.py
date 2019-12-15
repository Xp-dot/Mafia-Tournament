from django.shortcuts import render, get_object_or_404
from .models import Tournament, Team
from calendar import monthrange
from .forms import UserForm

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
    m_range = range(1,  monthrange(year, month)[1]+1)
    return render(request, "landing/calendar.html", {"m_range":m_range})


def rooster(request):
    return render(request, "landing/rooster.html", locals())


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

def rating(request):
    return render(request, "landing/rating.html", locals())