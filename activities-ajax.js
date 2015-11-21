$(document).ready(function(){
    $("input").addClass("form-control");

    // cont -> jogadas do dado
    // max --> limite máximo de jogadas
    var cont = 0;
    var max = 10;

    var cont_um_dado = 0;
    var cont_dois_dados = 0;

    // exibe dica ao passar o mouse sobre o elemento especificado
    $('[data-toggle="tooltip"]').tooltip();

    // a cada jogada, extrai o valor do dado e a fi e exibe os dados em html
    $('#dado').click(function(){
        d = new Date();
        $("#grafico").attr("src", "/activities/graficos/graf_um_dado.png?"+d.getTime());
        $("#numDado").removeClass();
        $(".progress").attr("class", "progress");
        $(".bg-primary").removeClass();
        if (cont < max) {
            $(".p1").attr("class", "p1 hidden");
            $(".p2").attr("class", "p2");
            $.get('/activities/jogar_dado/', function(data){
                var numDado = data.substring(0,1);
                var fi = data.substring(1,3);
                if (cont > 1) { $('#numDado').append(" - "); }
                $('#numDado').append(numDado)
                $('#'+(numDado-1)).addClass("bg-primary");
                $('#'+(numDado-1)).html(fi);
                $('#progressbar').attr("style", "width: "+(cont)+"0%");
                if (cont > 1) { $('.valores_dado').append(" - "); }
                $('.valores_dado').append(numDado);
                $('#img_dado').attr("src", "/static/images/dado"+numDado+".png");
            });
        } else {
            $(".p2").attr("class", "p2 hidden");
            $(".p3").attr("class", "p3");
            $("#proximo").attr("class", "btn btn-primary");
        };
        cont++;
    });

    var interrogacao = "<td><span class='glyphicon glyphicon-question-sign' aria-hidden='true'></span></td>";
    $("#fac5").replaceWith(interrogacao);
    $("#fr3").replaceWith(interrogacao);
    $("#facr4").replaceWith(interrogacao);

    questao_resposta("#questao1", "#resposta1", "#final_fi5");
    questao_resposta("#questao2", "#resposta2", "#final_fr2");
    questao_resposta("#questao3", "#resposta3", "#final_fac3");
    questao_resposta("#questao4", "#resposta4", "#final_facr3");



    // a cada jogada, extrai o valor do dado e a fi e exibe os dados em html
    $('#dois_dados').click(function(){
        cont_dois_dados++;
        if (cont_dois_dados == 1)
            $(".pos_central_info_1").attr("class", "pos_central_info_1");
        else if (cont_dois_dados > 1) {
            $(".pos_central_info_1").attr("class", "hidden");
            $(".pos_central_info_2").removeClass();
        }
            jogar_dados("#grafico2", "/activities/graficos/graf_dois_dados.png?", "/activities/jogar_dados/");
        if (cont_um_dado > 0) {
            exibeMensagem();            
        }

    });

    $("#um_dado").click(function(){
        cont_um_dado++;
        jogar_dados("#grafico1", "/activities/graficos/graf_um_dado.png?", "/activities/jogar_um_dado/" );
    });
});


// Exibe a mensagem relacionada a comparacao entre os graficos
function exibeMensagem() {
    $('#mensagem').attr("class", "alert alert-warning");
}

// exibe a resposta correta para cada questão
function questao_resposta(questao, resposta, campo_tabela) {
    $(questao).hover(function(){
        $(resposta).attr("class", "resposta");
        $(campo_tabela).addClass("bg-primary");
    },
    function(){
        $(resposta).attr("class", "hidden");
        $(campo_tabela).removeClass();
    });
}

function jogar_dados(id_grafico, end_grafico, url_jogar_dados) {
    d = new Date();
    $(id_grafico).attr("src", end_grafico+d.getTime());
    $.get(url_jogar_dados, function(data){
        $.each(data, function(key, value) {
            valor_fi = value;
            $("#fi_"+key).html(value);
        });
    });
}