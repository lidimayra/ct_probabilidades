# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from prob import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^binomial/$', views.binomial, name='binomial'),
                       url(r'^binomial_construcao/$', views.binomial_construcao, name='binomial_construcao'),
                       #url(r'^prob02/$', views.prob02, name='prob02'),
                       #url(r'^prob03/$', views.prob03, name='prob03'),
                       #url(r'^problema01/$', views.problema01, name='problema01'),
                       url(r'^jogar_dado/(?P<qtdeDados>[0-9]+)/(?P<n>[0-9]+)/$', views.jogar_dado, name='jogar_dado'),
                       url(r'^graficos/graf_um_dado.png$', views.graf_um_dado, name='graf_um_dado'),                   
                       url(r'^graficos/graf_dois_dados.png$', views.graf_dois_dados, name='graf_dois_dados'),
                       url(r'^graficos/graf_um_dado_moda.png$', views.graf_um_dado_moda, name='graf_um_dado_moda'),
                       url(r'^graficos/graf_dois_dados_moda.png$', views.graf_dois_dados_moda, name='graf_dois_dados_moda'),
                       url(r'^graficos/graf_binomial.png$', views.graf_binomial, name='graf_binomial'),
                       
                       url(r'^graficos/graf_construcao$', views.graf_construcao, name='graf_construcao'),

                       #url(r'^graficos/graf_binomial_construcao.png/(?P<valor1>[0-9]+)$', views.graf_binomial_construcao, name='graf_binomial_construcao'),
                       url(r'^graficos/graf_prob.png/(?P<valor1>[0-9]+)/(?P<operacao>[0-9]+)/(?P<valor2>[0-9]+)$', views.graf_prob, name='prob'),
                       )