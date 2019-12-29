from team_interactions.models import *

def accept_contract(contract_query, contract_id, new_value):
    contract = contract_query.filter(id=contract_id).first()
    player = contract.player.userprofile
    #Меняем статус контракта с Рассматривается на Принят
    contract.change_status(int(new_value))
    #Подписываем контракт пользователя(вступаем в команду)
    player.signup_contract(contract)
    #Отклоняем все контракты, которые имеют статус "Рассматривается"
    all_players_contract = Contract.objects.filter(player=player.user)
    for player_contract in all_players_contract.exclude(id=contract_id):
        if player_contract.contract_status == 1:
            player_contract.change_status(3)

def dismiss_contract(contract_query, contract_id, new_value):
    contract = contract_query.filter(id=contract_id).first()
    player = contract.player.userprofile
    #Игрок покидает команду
    player.revoke_contract()
    #Меняем статус контракта с Принят на Расторгнут
    contract.change_status(int(new_value))


def process_income_contract_request(request, income_contracts):
    new_value = request.POST.get('incoming')
    contract_id = request.POST.get('contract')
    if new_value == '2':
        accept_contract(income_contracts, contract_id, new_value)
    elif new_value == '5':
        dismiss_contract(income_contracts, contract_id, new_value)
    else:
        income_contracts.filter(id=contract_id).update(contract_status=new_value)

def process_outcome_contract_request(request, outcome_contracts):
    contract_id = request.POST.get('contract')
    new_value = request.POST.get('outgoing')
    outcome_contracts.filter(id=contract_id).update(contract_status=new_value)