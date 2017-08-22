from django.forms import ModelForm
from principal.models import Produto, Categoria


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'descricao',
            'quantidade',
            'preco',
            'data_fabricacao',
            'data_validade',
            'categoria'
        ]

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome',
            'descricao'
        ]