from django.conf.urls import url
from principal.views import *

urlpatterns = [
    url(r'^atualiza_login/(?P<id>\d+)/$', atualiza_login),

    url(r'^novo_produto/$', novo_produto),
    url(r'^lista_produto/$', lista_produto),
    url(r'^atualiza_produto/(?P<id>\d+)/$', atualiza_produto),
    url(r'^deleta_produto/(?P<id>\d+)/$', deleta_produto),

    url(r'^nova_categoria/$', nova_categoria),
    url(r'^lista_categoria/$', lista_categoria),
    url(r'^atualiza_categoria/(?P<id>\d+)/$', atualiza_categoria),
    url(r'^deleta_categoria/(?P<id>\d+)/$', deleta_categoria),

    url(r'^novo_fornecedor/$', novo_fornecedor),
    url(r'^lista_fornecedor/$', lista_fornecedor),
    url(r'^atualiza_fornecedor/(?P<id>\d+)/$', atualiza_fornecedor),
    url(r'^deleta_fornecedor/(?P<id>\d+)/$', deleta_fornecedor),

    url(r'^entrada_produto/$', entrada_produto),
    url(r'^saida_produto/$', saida_produto),
    url(r'^lista_movimento/$', lista_movimento),
    url(r'^lista_lote/$', lista_lote),

    url(r'^ajax/get_produto/$', get_produto),
    url(r'^ajax/get_lote/$', get_lote),
    url(r'^ajax/get_qtdelote/$', get_qtdelote),

    url(r'^home/$', home),
]
