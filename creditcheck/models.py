from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    salario = models.FloatField()
    nivel_escolar = models.CharField(max_length=255)
    quantidade_cartoes = models.IntegerField()
    dividas = models.FloatField()
    saldo = models.FloatField()
