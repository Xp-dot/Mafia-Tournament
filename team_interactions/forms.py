from django import forms
from django.core.exceptions import ValidationError
from .models import Contract, Team

class ContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.is_valid()
        salary_temp = 300-100*Team.objects.get(name=self.cleaned_data['team']).league
        self.fields['salary'].widget.attrs['min'] = salary_temp

    def clean_contract_value(self):
        contract_value = self.cleaned_data['contract_value']
        salary = self.cleaned_data['salary']
        if contract_value < salary*2:
            raise ValidationError("Стоимость контракта меньше двух зарплат!")
        elif contract_value < 100:
            raise ValidationError("Стоимость контракта меньше 100 маф, жлобская сучара!")
        return contract_value

    class Meta:
        model = Contract
        fields = ['player', 'team_owner', 'team', 'salary', 'contract_value', 'duration', 'contract_status', 'played_game_bonus', 'victory_coef']
        widgets = {'contract_status': forms.HiddenInput()}
        labels = {
            'player': 'Ник игрока', 'team_owner': 'Владелец команды', 'team': 'Команда', 'salary': 'Зарплата', 'contract_value': 'Стоимость контракта', 'duration': 'Длительность', 'played_game_bonus': 'Бонус за сыгранную партию', 'victory_coef': 'Коэффициент за победу'
        }
        help_texts = {
            'salary': 'Введите зарплату игрока','contract_value': 'Введите сумму, за которую игрок сможет выкупить свой контракт', 'duration': 'Введите к-во сезонов(турниров) пребывания игрока в команде'
        }