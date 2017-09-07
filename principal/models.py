# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import DateTimeField
from django.db.models.signals import post_save


class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    descricao = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descrição')
    data_cadastro = DateTimeField(verbose_name=u'Data Cadastro', auto_now_add=True, editable=False)
    data_alteracao = DateTimeField(verbose_name=u'Data Alteração', auto_now=True, editable=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome')
    descricao = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descrição')
    quantidade = models.IntegerField(null=False, default=0, blank=False, validators=[MinValueValidator(0)],
                                     editable=False, verbose_name='Quantidade')
    preco_unitario = models.FloatField(null=True, blank=True, verbose_name='Preço Unitário',
                                       validators=[MinValueValidator(0)])
    data_cadastro = DateTimeField(verbose_name=u'Data Cadastro', auto_now_add=True, editable=False)
    data_alteracao = DateTimeField(verbose_name=u'Data Alteração', auto_now=True, editable=False)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria')

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome Fantasia')
    data_cadastro = DateTimeField(verbose_name=u'Data Cadastro', auto_now_add=True, editable=False)
    data_alteracao = DateTimeField(verbose_name=u'Data Alteração', auto_now=True, editable=False)

    def __str__(self):
        return self.nome_fantasia


class EntradaProduto(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descrição')
    lote = models.CharField(max_length=50, null=False, blank=False, verbose_name='Lote')
    fornecedor = models.ForeignKey(Fornecedor, verbose_name='Fornecedor')
    produto = models.ForeignKey(Produto, verbose_name='Produto')
    quantidade_inicial = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)],
                                             verbose_name='Qtde. Inicial')
    quantidade = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)],
                                     verbose_name='Quantidade')
    data_cadastro = DateTimeField(verbose_name=u'Data Entrada', auto_now_add=True, editable=False)
    data_fabricacao = models.DateField(null=True, blank=True, verbose_name='Data de Fabricação')
    data_validade = models.DateField(null=True, blank=True, verbose_name='Data de Validade')
    usuario = models.ForeignKey(User, verbose_name='Usuário', editable=False)

    def __str__(self):
        return self.lote


class SaidaProduto(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False, verbose_name='Descrição')
    entrada = models.ForeignKey(EntradaProduto, verbose_name='Lote')
    quantidade = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(1)],
                                     verbose_name='Quantidade')
    data_cadastro = DateTimeField(verbose_name=u'Data Saída', auto_now_add=True, editable=False)
    usuario = models.ForeignKey(User, verbose_name='Usuário', editable=False)

    def __str__(self):
        return self.descricao


from .signals import post_save_entrada, post_save_saida

post_save.connect(post_save_entrada, sender=EntradaProduto)
post_save.connect(post_save_saida, sender=SaidaProduto)
