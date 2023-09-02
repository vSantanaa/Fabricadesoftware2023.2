from django.db import models

class Funcionarios(models.Model):
    funcionario = models.CharField(max_length=150)
    funcao = models.CharField(max_length=150)
    idade = models.IntegerField()
