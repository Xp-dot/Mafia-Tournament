
console.log('js launched');

window.onload =  function(){
    $('#id_player').prop('disabled', 'disabled');
    $('#id_team_owner').prop('disabled', true);
    $('#id_team').prop('disabled', true);
    $('#contract_form').append('<input id="id_player" type="hidden" name="player" required=""/>');
    $('input#id_player').val($('select#id_player').val());
    $('#contract_form').append('<input id="id_team_owner" type="hidden" name="team_owner" value="myvalue" required=""/>');
    $('input#id_team_owner').val($('select#id_team_owner').val());
    $('#contract_form').append('<input id="id_team" type="hidden" name="team" value="myvalue" required=""/>');
    $('input#id_team').val($('select#id_team').val());
};
