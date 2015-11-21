# -*- coding: utf-8 -*-
import simplejson
from random import randint
from funcoes import *
from django.http import HttpResponse
from django.shortcuts import render

xi1 = [1, 2, 3, 4, 5, 6]
fi1 = [0, 0, 0, 0, 0, 0]

xi2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
fi2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

xi = []
pi = []

def jogar_dado(request, qtdeDados, n):
    if int(qtdeDados) == 1:
        fi = fi1
        xi = xi1
    else:
        fi = fi2
        xi = xi2
    for valor in range(len(fi)):
        fi[valor] = 0
    for aux in range(int(n)):
        total = randint(1,6)
        if int(qtdeDados) > 1:
            dado2 = randint(1,6)
            total += dado2
        for valor in range(len(xi)):
            if xi[valor] == total:
                fi[valor] += 1
    response_data = simplejson.dumps(fi)
    return HttpResponse(response_data, content_type='application/json')

def index(request):
    zerarFi(fi1, fi2)
    return render(request, "prob/index.html", {})
    
def binomial(request):
    zerarFi(fi1, fi2)
    return render(request, "prob/binomial.html", {})
    
def binomial_construcao(request):
    return render(request, "prob/binomial_construcao.html", {})

def graf_um_dado(request):
    response = grafico(xi1, fi1, '', '', '')
    return response

def graf_dois_dados(request):
    response = grafico(xi2, fi2, '', '', '')
    return response
    
def graf_um_dado_moda(request):
    response = grafico(xi1, fi1, 'moda', '', '')
    return response

def graf_dois_dados_moda(request):
    response = grafico(xi2, fi2, 'moda', '', '')
    return response

def graf_prob(request, valor1, operacao, valor2):
    response = grafico(xi2, fi2, valor1, operacao, valor2)
    return response
    
def graf_binomial(request):
    response = grafico(xi2, fi2, '', '', '')
    return response
    
def graf_construcao(request):
    x = [0, 1, 2, 3, 4, 5]
    y = [1.02, 7.68, 0, 0, 0, 0]
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    
    barlist = ax.bar(x, y, 0.9, align="center")

    ax.set_xlim(-1,max(x)+1)
    ax.set_ylim(0, 20)
    
    # ax.set_title('Jogadas')
    ax.grid(True)
    
    response = HttpResponse(content_type='image/png')
    canvas.print_figure(response) # print_png
    return response

"""def prob02(request):
    zerarFi(fi1, fi2)
    return render(request, "prob/prob02.html", {})

def prob03(request):
    zerarFi(fi1, fi2)
    return render(request, "prob/prob03.html", {})
    
def problema01(request):
    zerarFi(fi1, fi2)
    return render(request, "prob/problema01.html", {})
"""