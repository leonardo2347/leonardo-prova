from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=11)
    idade = models.IntegerField()

class Produto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=11)
    valor = models.CharField(max_length=1)

class Carrinho_De_Compras(models.Model):
    supermercado = models.CharField(max_length=50)
    capacidade = models.CharField(max_length=11)
    preco = models.IntegerField()
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)



















