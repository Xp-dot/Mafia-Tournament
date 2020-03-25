from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import UserProfile
from team_interactions.contract_utils import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form' : form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def team_management(request):
    if request.user.is_authenticated:
        my_teams = Team.objects.filter(owner=request.user)
        if request.method == 'POST':
            usr = request.POST.get('player')
            usr_obj = UserProfile.objects.filter(user=usr)[:1].get()
            usr_obj.change_reserve_state()
        context = {'my_teams': my_teams}
    return render(request, 'users/profile_my_owned_teams.html', context)

@login_required
def my_contracts(request):
    outcome_contracts = Contract.objects.filter(player=request.user)
    income_contracts = Contract.objects.filter(team_owner=request.user)
    if request.method == 'POST':
        if request.POST.get('outgoing'):
            process_outcome_contract_request(request, outcome_contracts)
        elif request.POST.get('incoming'):
            process_income_contract_request(request, income_contracts)
    context = {'team_enroll_contract': outcome_contracts, 'team_request_contract': income_contracts}
    return render(request, 'users/profile_my_contracts.html', context)

@login_required
def my_team(request):
    if request.user.is_authenticated:
        player = UserProfile.objects.filter(user=request.user)[:1].get()
        players_in_team = UserProfile.objects.filter(team=player.team)
        context = {'team':player.team,'players_in_team': players_in_team}
    return render(request, 'users/profile_my_team.html', context)