from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['player', 'team_owner', 'team', 'salary', 'contract_value', 'duration', 'contract_status']
        widgets = {'contract_status': forms.HiddenInput()}
        labels = {
            'player': 'Ник игрока', 'team_owner': 'Владелец команды', 'team': 'Команда', 'salary': 'Зарплата', 'contract_value': 'Стоимость контракта', 'duration': 'Длительность'
        }
        help_texts = {
            'salary': 'Введите зарплату игрока','contract_value': 'Введите сумму, которая будет уплачена инициатором разрыва контракта', 'duration': 'Введите к-во сезонов(турниров) пребывания игрока в команде'
        }