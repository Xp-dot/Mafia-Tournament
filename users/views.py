from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from team_interactions.models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {'form' : form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def team_management(request):
    return render(request, 'users/profile_my_owned_teams.html')

@login_required
def my_contracts(request):
    team_enroll = Contract.objects.filter(player=request.user)
    team_request = Contract.objects.filter(team_owner=request.user)
    if request.method == 'POST':
        contract_id = request.POST.get('contract')
        if request.POST.get('outgoing'):
            new_value = request.POST.get('outgoing')
            team_enroll.filter(id=contract_id).update(contract_status=new_value)
        elif request.POST.get('incoming'):
            new_value = request.POST.get('incoming')
            team_request.filter(id=contract_id).update(contract_status=new_value)
    context = {'team_enroll_contract': team_enroll, 'team_request_contract': team_request}
    return render(request, 'users/profile_my_contracts.html', context)

@login_required
def my_team(request):
    return render(request, 'users/profile_my_team.html')