# -*- coding: utf-8 -*-
from math import floor
from decimal import Decimal, getcontext
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def zerarFi(fi1, fi2):
    for aux in range(6):
        fi1[aux] = 0
    for aux in range(12):
        fi2[aux] = 0

def grafico(x, y, valor1, operacao, valor2):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    
    barlist = ax.bar(x, y, 0.9, align="center")
    if (valor1 == 'moda'):
        destacarModa(y, barlist)
        #ax.set_title(destaque)
    elif (valor1):
        v1 = int(valor1)-1
        v2 = int(valor2)-1
        destacarProb(v1, barlist, operacao, v2)
    ax.set_xlim(0,max(x)+1)
    ax.set_ylim(0, (max(y)+20))
    
    # ax.set_title('Jogadas')
    ax.grid(True)
    ax.set_xlabel('xi')
    ax.set_ylabel('fi')
    
    response = HttpResponse(content_type='image/png')
    canvas.print_figure(response) # print_png
    return response

def destacarModa(y, barlist):
    i_moda = y.index(max(y))
    barlist[i_moda].set_color('r')

def destacarProb(valor, barlist, operacao, valor2):
    for aux in range(12):
        if (valor > 0):
            if operacao == "1":
                if (aux > valor):
                    barlist[aux].set_color('r')
            elif operacao == "2":
                if (aux >= valor):
                    barlist[aux].set_color('r')
            elif operacao == "3":
                if (aux < valor):
                    barlist[aux].set_color('r')
            elif operacao == "4":
                if (aux <= valor):
                    barlist[aux].set_color('r')
            elif operacao == "5":
                if (aux > valor and aux < valor2):
                    barlist[aux].set_color('r')
            elif operacao == "6":
                if (aux >= valor and aux <= valor2):
                    barlist[aux].set_color('r')

def destacarMediana(xi, fi, barlist):
    mediana = 0
    #fac = 0
    """
    em = float(sum(fi)+1)/2 
    for aux in range(len(fi)):       
        fac += fi[aux]
        if em > fac[aux]:
            if sum(fi)%2==0:
                if floor(em) == xi[aux]:
                    mediana = float(xi[aux]+xi[aux+1])/2
                else:
                    mediana = xi[aux+1]
            else:
                mediana = xi[aux+1]
    """
    """
    i_media = fi.index(mediana)
    barlist[i_media].set_color('r')
    """
    
def freq(fi):
    getcontext().prec = 4
    res = {
        'fac': [],
        'fac_soma': [],
        'fr': [],
        'facr': []
    }
    fac = 0
    for aux in range (len(fi)):
        fac += fi[aux]
        fr = (Decimal(fi[aux]) / sum(fi) * 100)
        facr = Decimal(fac) / sum(fi) * 100
        res['fac'].append(fac)
        res['fr'].append(fr)
        res['facr'].append(facr)
    return res

# Calculo das medidas de posicao central (Media, Moda e Mediana).
def posicao(xi, fi):
    dict = {
        'media': 0,
        'moda': 0,
        'mediana': 0
    }
    em = float(sum(fi)+1)/2    
    fac = freq(fi)['fac']    
    for aux in range(len(fi)):       
        dict['media'] += float(xi[aux]*fi[aux])
        if em > fac[aux]:
            if sum(fi)%2==0:
                if floor(em) == xi[aux]:
                    dict['mediana'] = float(xi[aux]+xi[aux+1])/2
                else:
                    dict['mediana'] = xi[aux+1]
            else:
                dict['mediana'] = xi[aux+1]
    dict['media'] /= sum(fi)
    dict['moda'] = xi[fi.index(max(fi))]
    return dict
    
def media(xi, fi):
    media = 0.0
    for aux in range(len(fi)):
        media += (xi[aux] * fi[aux])
    media /= sum(fi)
    return media

# Exemplo 1 - Peso
# xi = [48, 52, 65, 67, 68, 70, 75, 76, 77, 85, 96, 97, 98]
# fi = [1, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1]; pop = True
"""
xi = [1, 2, 3, 4, 5, 6]
fi = [0, 0, 0, 0, 0, 0]
"""


# Exemplo 2 - Chuva
xi = [30, 50, 60, 90, 110]; fi = [3, 7, 12, 8, 2]; pop = False

# Exercicio 1
# xi = [36, 40, 41, 44, 46]; fi = [3, 10, 13, 9, 4]; pop = False

# Exercicio 2
# xi = [10, 13, 15, 17, 20]; fi = [6, 6, 14, 8, 6]; pop = True

# Exercicio 3
# xi = [10, 12, 15, 16, 20]; fi = [2, 3, 6, 4, 1]; pop = False