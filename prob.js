$(document).ready(function(){
    $("input").addClass("form-control");

    // quando esses métodos estão habilitados, os gráficos não travam
    $("#btn_dado01").click(function(){
        var img_grafico = "graf_um_dado";
        if ($("#cb_moda01").is(":checked"))
            img_grafico += "_moda";            
        jogar_dados("#grafico1", "/prob/graficos/"+ img_grafico +".png?", "/prob/jogar_dado/1/");
    });
    $("#btn_dado02").click(function(){
        var img_grafico = "graf_dois_dados";
        if ($("#cb_moda02").is(":checked"))
            img_grafico += "_moda";
        jogar_dados("#grafico2", "/prob/graficos/" + img_grafico + ".png?", "/prob/jogar_dado/2/");
    });
    $('#btn_binomial').click(function(){
        jogar_dados("#graf_binomial", "/prob/graficos/graf_binomial.png?", "/prob/jogar_dado/2/");
    });
    // ----- fim -----

    $("#btn_dado01").click(function(){
        var n = $("#n01").val();
        var img_grafico = "graf_um_dado";
        if ($("#cb_moda01").is(":checked"))
            img_grafico += "_moda";            
        jogar_dados("#grafico1", "/prob/graficos/"+ img_grafico +".png?", "/prob/jogar_dado/1/" + n);
    });

    $('#btn_dado02').click(function(){
        var n = $("#n02").val();
        var img_grafico = "graf_dois_dados";
        if ($("#cb_moda02").is(":checked"))
            img_grafico += "_moda";
        jogar_dados("#grafico2", "/prob/graficos/" + img_grafico + ".png?", "/prob/jogar_dado/2/" + n);
    });

    $('#btn_binomial').click(function(){
        var n = $("#n").val();
        jogar_dados("#graf_binomial", "/prob/graficos/graf_binomial.png?", "/prob/jogar_dado/2/" + n);
    });

    $('#btn_maior').click(function(){
        var valor = $("#maior").val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_prob.png/"+valor+"/1/0");
    });

    $('#btn_minimo').click(function(){
        var valor = $("#minimo").val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_prob.png/"+valor+"/2/0");
    });

    $('#btn_menor').click(function(){
        var valor = $("#menor").val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_prob.png/"+valor+"/3/0");
    });

    $('#btn_maximo').click(function(){
        var valor = $("#maximo").val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_prob.png/"+valor+"/4/0");
    });

    $('#btn_entre').click(function(){
        var valor1 = $("#entre01").val();
        var valor2 = $("#entre02").val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_prob.png/"+valor1+"/5/"+valor2);
    });

    $('#btn_de').click(function(){
        var valor1 = $("#de01").val();
        var valor2 = $("#de02").val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_prob.png/"+valor1+"/6/"+valor2);
    });


    $('.pi').click(function(){
        teste = $(this).val();
        $("#graf_binomial").attr("src", "/prob/graficos/graf_binomial_construcao.png/"+teste);
    });
});

function destacar_moda01() {
    if ($("#cb_moda01").is(":checked")) {
         $("#grafico1").attr("src", "/prob/graficos/graf_um_dado_moda.png");
    } else {
        $("#grafico1").attr("src", "/prob/graficos/graf_um_dado.png");
    }
} 

function destacar_moda02() {
    if ($("#cb_moda02").is(":checked")) {
         $("#grafico2").attr("src", "/prob/graficos/graf_dois_dados_moda.png");
    } else {
        $("#grafico2").attr("src", "/prob/graficos/graf_dois_dados.png");
    }
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