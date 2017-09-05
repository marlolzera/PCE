from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms, CharField, TextInput, Textarea, ModelChoiceField
from principal.models import *


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'descricao',
            'categoria',
            'preco_unitario',
        ]

    descricao = CharField(max_length=200, label=u'Descrição',
                          widget=Textarea(attrs={'cols': 40,
                                                 'rows': 5,
                                                 # 'placeholder': 'Descrição',
                                                 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome',
            'descricao'
        ]

    descricao = CharField(max_length=200, label=u'Descrição',
                          widget=Textarea(attrs={'cols': 40,
                                                 'rows': 5,
                                                 # 'placeholder': 'Descrição',
                                                 'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nome_fantasia'
        ]

    def __init__(self, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'


class EntradaProdutoForm(ModelForm):
    class Meta:
        model = EntradaProduto
        fields = [
            'descricao',
            'fornecedor',
            'categoria',
            'produto',
            'quantidade'
        ]

    fornecedor = ModelChoiceField(queryset=Fornecedor.objects.all(), label=u'Fornecedor',
                                  empty_label="--- Selecione ---")
    categoria = ModelChoiceField(queryset=Categoria.objects.all(), label=u'Categoria', empty_label="--- Selecione ---")
    produto = ModelChoiceField(queryset=Produto.objects.none(), label=u'Produto', empty_label=None)

    def __init__(self, *args, **kwargs):
        super(EntradaProdutoForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'

        if self.initial.get("categoria"):
            produto = self.fields['produto']
            produto.queryset = Produto.objects.filter(categoria_id=self.initial.get("categoria"))


class SaidaProdutoForm(ModelForm):
    class Meta:
        model = SaidaProduto
        fields = [
            'descricao',
            'categoria',
            'produto',
            'quantidade'
        ]

    def __init__(self, *args, **kwargs):
        super(SaidaProdutoForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'

        if self.initial.get("categoria"):
            produto = self.fields['produto']
            produto.queryset = Produto.objects.filter(categoria_id=self.initial.get("categoria"))

    def clean_quantidade(self):
        produto = self.cleaned_data['produto']
        qtde = self.cleaned_data['quantidade']

        if qtde > produto.quantidade:
            raise ValidationError(u"Quantidade indisponível!")
        else:
            return qtde
