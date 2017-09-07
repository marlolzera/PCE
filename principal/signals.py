from principal.models import Produto, EntradaProduto


def post_save_entrada(instance, created, *args, **kwargs):
    # created: True se foi registro novo (False se foi update)
    if created:
        # soma qtde produto
        produto = Produto.objects.get(id=instance.produto_id)
        produto.quantidade = produto.quantidade + instance.quantidade_inicial
        produto.save()


def post_save_saida(instance, created, *args, **kwargs):
    # created: True se foi registro novo (False se foi update)
    if created:
        # subtrai qtde atual da entrada/lote
        lote = EntradaProduto.objects.get(id=instance.entrada_id)
        lote.quantidade = lote.quantidade - instance.quantidade
        lote.save()

        # subtrai qtde do produto
        entrada = EntradaProduto.objects.get(id=instance.entrada_id)
        produto = Produto.objects.get(id=entrada.produto_id)
        produto.quantidade = produto.quantidade - instance.quantidade
        produto.save()
