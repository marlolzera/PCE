# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from principal.models import Produto
from principal.forms import ProdutoForm, CategoriaForm
from django.shortcuts import render, redirect
from django.shortcuts import render

def home(request):
    return render(request, 'principal/index.html')


def novoProduto(request):
    form = ProdutoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(listaProduto)

    return render(request, 'principal/novoProduto.html', {'form': form})


def novaCategoria(request):
    form = CategoriaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(listaProduto)

    return render(request, 'principal/novaCategoria.html', {'form': form})


def listaProduto(request):
    # fazer uma consulta personalizada para trazer tbm o nome da categoria

    # SELECT
    #     P. *,
    #     C.nome AS "categoria"
    # FROM PRINCIPAL_PRODUTO P
    # LEFT JOIN PRINCIPAL_CATEGORIA C ON
    #     P.categoria_id = C.id
    # ORDER BY
    #     P.id DESC
    lista_produto = Produto.objects.all().order_by('-id')
    return render(request, 'principal/listaProduto.html', {'lista_produto': lista_produto})


def atualizaProduto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(listaProduto)

    return render(request, 'principal/novoProduto.html', {'form': form})


def deletaProduto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(listaProduto)

