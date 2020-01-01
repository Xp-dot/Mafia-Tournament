from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContractForm

# Create your views here.
def get_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_contracts')
        else:
            print('form is not valid')
            print(form.errors)
    else:
        print('method is not post')
        form = ContractForm()
    return render(request, "team_interactions/contract_page.html", {'form': form})


@login_required
def profile(request):
    return  render(request, 'users/profile.html')