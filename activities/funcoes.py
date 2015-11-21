# -*- coding: utf-8 -*-
from activities.estatistica import freq, posicao

def main(xi, fi):
    freqs = freq(fi)
    pos = posicao(xi, fi)
    context_dict = {
        'n': sum(fi),
        'fac': freqs['fac'],
        'fac_soma': freqs['fac_soma'],
        'fr': freqs['fr'],
        'facr': freqs['facr'],
        'media': pos['media'],
        'moda': pos['moda'],
        'mediana': pos['mediana'],
        'lista': zip(xi, fi)
    }
    return context_dict

def exibir_form(request, campo, id_form, xi, fi):
    form = campo(request.POST)
    context_dict = main(xi, fi)
    if request.method == 'POST':
        resposta_usuario = request.POST[id_form]        
        resposta_correta = checar_resposta(xi, fi, id_form)        
        if form.is_valid() and resposta_usuario == str(resposta_correta):
            context_dict['acerto'] = "Resposta correta! Clique no botão para avançar."
        else:
            context_dict['erro'] = "Resposta incorreta! Tente novamente."
    else:
        form = campo()
    context_dict['form'] = form
    return context_dict

def checar_resposta(xi, fi, valor):
    tabela = main(xi, fi)
    if valor == "n":
        res = tabela['n']
    elif valor == 'fac':
        res = tabela['fac'][4]
    elif valor == 'fr':
        res = tabela['fr'][2]
    elif valor == 'facr':
        res = tabela['facr'][3]
    return res