from django.conf.urls import patterns, url
from activities import views

urlpatterns = patterns('',
                       url(r'^jogar_dado/$', views.jogar_dado, name='jogar_dado'),
                       url(r'^espaco_amostral/$', views.espaco_amostral, name='espaco_amostral'),
                       url(r'^$', views.index, name='index'),
                       url(r'^fac/$', views.fac, name='fac'),
                       url(r'^fr/$', views.fr, name='fr'),
                       url(r'^facr/$', views.facr, name='facr'),
                       url(r'^graficos/graf_um_dado.png$', views.graf_um_dado, name='graf_um_dado'),
                       url(r'^tabela_frequencias/$', views.tabela_frequencias, name="tabela_frequencias"),
                       url(r'^posicao_central/$', views.posicao_central, name="posicao_central"),
                       url(r'^jogar_um_dado/$', views.jogar_um_dado, name='jogar_um_dado'),
                       url(r'^jogar_dados/$', views.jogar_dois_dados, name="jogar_dois_dados"),
                       url(r'^graficos/graf_dois_dados.png$', views.graf_dois_dados, name="graf_dois_dados"),
                       url(r'^media/$', views.media, name="media"),
                       url(r'^probabilidade/$', views.probabilidade, name="probabilidade"),
                       url(r'^prob02/$', views.prob02, name="prob02"),
                       )