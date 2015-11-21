from django.shortcuts import render

def suposicao_probabilidades(request):
    return render(request, 'artigos/suposicao_probabilidades.html', {})
