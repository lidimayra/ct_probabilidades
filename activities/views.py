# -*- coding: utf-8 -*-
import simplejson
from random import randint
from django.http import HttpResponse
from django.shortcuts import render
from activities.forms import *
from activities.funcoes import main, exibir_form

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

xi1 = [1, 2, 3, 4, 5, 6]
fi1 = [0, 0, 0, 0, 0, 0]

xi2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
fi2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# construção do gráfico ao jogar um único dado.
def graf_um_dado(request):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    
    barlist = ax.bar(xi1, fi1, 0.9, align="center")
    #i_moda = fi1.index(max(fi1))
    #barlist[i_moda].set_color('r')
    ax.set_xlim(0,7)
    ax.set_ylim(0, (max(fi1)+1))
    
    ax.set_title('Jogadas')
    ax.grid(True)
    ax.set_xlabel('xi')
    ax.set_ylabel('fi')
    
    response = HttpResponse(content_type='image/png')
    canvas.print_figure(response) # print_png
    return response

def jogar_dado(request):
    response = HttpResponse()
    dado = randint(1,6)
    response.write(dado)
    for valor in range(len(xi1)):
        if xi1[valor] == dado:
            fi1[valor]+=1
            response.write(fi1[valor])
    return response

def index(request):
    for aux in range(len(xi1)):
        fi1[aux] = 0
    context_dict = { 'lista': zip(xi1, fi1) }
    return render(request, "activities/index.html", context_dict)

def espaco_amostral(request):
    context_dict = exibir_form(request, form_n, 'n', xi1, fi1)
    return render(request, "activities/espaco_amostral.html", context_dict)

def fac(request):
    context_dict = exibir_form(request, form_fac, 'fac', xi1, fi1)
    fac_soma = []
    for aux in range(len(fi1)):
        if aux == 0:
            res = str(fi1[aux])+ " + 0"
        else:
            res = str(fi1[aux])+ " + "+str(context_dict['fac'][aux-1])
        fac_soma.append(res)
    context_dict['lista'] = zip(xi1, fi1,  fac_soma, context_dict['fac'])
    return render(request, "activities/fac.html", context_dict)

def fr(request):
    context_dict = exibir_form(request, form_fr, 'fr', xi1, fi1) 
    context_dict['lista'] = zip(xi1, fi1, context_dict['fr'])
    return render(request, "activities/fr.html", context_dict)
    
def facr(request):
    context_dict = exibir_form(request, form_facr, 'facr', xi1, fi1)        
    context_dict['lista'] = zip(xi1, context_dict['fac'], context_dict['facr'])
    return render(request, "activities/facr.html", context_dict)

def tabela_frequencias(request):
    context_dict = main(xi1, fi1)
    context_dict['acerto'] = "Quando estiver pronto clique no botão para avançar."
    context_dict['lista'] = zip(xi1, fi1, context_dict['fr'], context_dict['fac'], context_dict['facr'])
    context_dict['resposta1'] = fi1[4]
    context_dict['resposta2'] = context_dict['fr'][1]
    context_dict['resposta3'] = context_dict['fac'][2]
    context_dict['resposta4'] = context_dict['facr'][5] - context_dict['facr'][2]
    return render(request, "activities/tabela_frequencias.html", context_dict)

def posicao_central(request):
    for aux in range(12):
        fi2[aux] = 0
    context_dict = {
        'xi': xi2,
        'fi': fi2,
        'n': sum(fi2),
        'lista': zip(xi2, fi2)
    }
    return render(request, "activities/posicao_central.html", context_dict)

def jogar_dados(request):
    for valor in range(len(fi)):
        fi2[valor] = 0
    for aux in range(800):
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        total = dado1 + dado2
        for valor in range(len(xi)):
            if xi2[valor] == total:
                fi2[valor] += 1
    response_data = simplejson.dumps(fi2)
    return HttpResponse(response_data, content_type='application/json')

def graf_dois_dados(request):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    barlist = ax.bar(xi2, fi2, 0.9, align="center")
    i_moda = fi2.index(max(fi2))
    barlist[i_moda].set_color('r')
    ax.set_xlim(0,max(xi2)+1)
    ax.set_ylim(0, (max(fi2)+30))
    ax.set_title('Jogadas')
    ax.grid(True)
    ax.set_xlabel('xi')
    ax.set_ylabel('fi')
    
    response = HttpResponse(content_type='image/png')
    canvas.print_figure(response) # print_png
    return response

def media(request):
    context_dict = main(xi2, fi2)
    fixi_mult = []
    fixi = []
    for aux in range(len(fi2)):
        fixi_mult.append(str(fi2[aux])+" x "+str(xi2[aux]))
        fixi.append(fi2[aux] * xi2[aux])
    context_dict['lista'] = zip(xi2, fi2, fixi_mult, fixi)
    context_dict['sum_fixi'] = sum(fixi)
    return render(request, "activities/media.html", context_dict)

def probabilidade(request):
    for aux in range(6):
        fi1[aux] = 0
    for aux in range(12):
        fi2[aux] = 0
    return render(request, "activities/probabilidade.html", {})

def prob02(request):
    for aux in range(6):
        fi1[aux] = 0
    for aux in range(12):
        fi2[aux] = 0
    return render(request, "activities/prob02.html", {})

def jogar_um_dado(request):
    for valor in range(len(fi1)):
        fi1[valor] = 0     
    for aux in range(3000):
        dado = randint(1, 6)
        for valor in range(len(xi1)):
            if xi1[valor] == dado:
                fi1[valor]+=1
    response_data = simplejson.dumps(fi1)
    return HttpResponse(response_data, content_type='application/json')

def jogar_dois_dados(request):
    for valor in range(len(fi2)):
        fi2[valor] = 0    
    for aux in range(3000):
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        total = dado1 + dado2
        for valor in range(len(xi2)):
            if xi2[valor] == total:
                fi2[valor] += 1
    response_data = simplejson.dumps(fi2)
    return HttpResponse(response_data, content_type='application/json')