from django.db import models

class Filme(models.Model):
    nome_filme = models.CharField(max_length=40)
    imagem_font = models.TextField()
    em_alta = models.BooleanField()
    em_cartaz = models.BooleanField()
