# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from artigos import views

urlpatterns = patterns('',
                       url(r'^$', views.suposicao_probabilidades, name='suposicao_probabilidades'))