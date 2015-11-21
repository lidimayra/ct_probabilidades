# -*- coding: utf-8 -*-
from random import randint
import simplejson

xi2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fi2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]


to_json = []
    
for aux in fi2:
    dict_teste = {}
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    total = dado1 + dado2

    for valor in range(len(xi2)):
        if xi2[valor] == total:
            fi2[valor] += 1
            dict_teste[valor] = fi2[valor]

to_json.append(fi2)

response_data = simplejson.dumps(to_json)

print response_data