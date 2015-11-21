from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    #slug = models.SlugField(unique=True)
    
    def __unicode__(self):
        return self.nome

class Conteudo(models.Model):
    disciplina = models.ForeignKey(Disciplina)
    titulo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titulo