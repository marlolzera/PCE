from django.conf.urls import url
from principal.views import home, novoProduto, novaCategoria, listaProduto, atualizaProduto, deletaProduto


urlpatterns = [
    url(r'^$',home, name='home'),
    url(r'^novoProduto/$',novoProduto, name='novoProduto'),
    url(r'^novaCategoria/$',novaCategoria, name='novaCategoria'),
    url(r'^listaProduto/$',listaProduto, name='listaProduto'),
    url(r'^atualizaProduto/(?P<id>\d+)/$',atualizaProduto, name='atualizaProduto'),
    url(r'^deletaProduto/(?P<id>\d+)/$',deletaProduto, name='deletaProduto'),
]