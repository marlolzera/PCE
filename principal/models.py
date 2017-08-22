# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator



class Categoria(models.Model):
    nome = models.CharField(max_length=50, default='categoria', null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50, default='produto', null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(null=False, default=1, blank=False, validators=[MinValueValidator(1)])
    preco = models.FloatField(null=True, blank=True)
    data_fabricacao = models.DateField(null=True, blank=True)
    data_validade = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, default=1)

    def __str__(self):
        return self.nome
