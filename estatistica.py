# -*- coding: utf-8 -*-
from math import floor
from decimal import Decimal, getcontext

# Calculo da Frequencia Acumulada, Frequencia Relativa e Frequencia Acumulada
# Relativa. Retorna os valores como listas.
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

# Calculo das medidas de dispersao (Variancia, Desvio Padrao e Coeficiente
# de Variacao)
def dispersao(xi, fi, pop):
    dict = {
        'variancia': 0,
        'desvio_padrao': 0,
        'cv': 0
    }
    media = posicao(xi, fi)['media']    
    soma = 0
    n = sum(fi)
    for i in range(len(fi)):
        aux = fi[i]*(xi[i] - media)**2
        soma += aux
    if pop:
        dict['variancia'] = soma / n
    else:
        dict['variancia'] = soma / (n-1)
    dict['desvio_padrao'] = dict['variancia']**0.5
    dict['cv'] = dict['desvio_padrao']/media    
    return dict

# Exemplo 1 - Peso
xi = [48, 52, 65, 67, 68, 70, 75, 76, 77, 85, 96, 97, 98]
fi = [1, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1]; pop = True
"""
xi = [1, 2, 3, 4, 5, 6]
fi = [0, 0, 0, 0, 0, 0]
"""
# Exemplo 2 - Chuva
# xi = [30, 50, 60, 90, 110]; fi = [3, 7, 12, 8, 2]; pop = False

# Exercicio 1
# xi = [36, 40, 41, 44, 46]; fi = [3, 10, 13, 9, 4]; pop = False

# Exercicio 2
# xi = [10, 13, 15, 17, 20]; fi = [6, 6, 14, 8, 6]; pop = True

# Exercicio 3
# xi = [10, 12, 15, 16, 20]; fi = [2, 3, 6, 4, 1]; pop = False

#print freq(fi)
print posicao(xi, fi)['media']
#print dispersao(xi, fi, pop)

"""plt.bar(xi, fi)
plt.xlabel("xi")
plt.ylabel("fi")
plt.axis([1, 7, 1, 5])
plt.show()"""

def jogar_dado_40():
    from random import randint
    for aux in range(35):
        dado = randint(1,6)
        for valor in range(len(xi)):
            if xi[valor] == dado:
                fi[valor]+=1
    return fi
    
# print jogar_dado_40()