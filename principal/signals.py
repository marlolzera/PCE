from principal.models import Produto


def post_save_entrada(instance, created, *args, **kwargs):
    # created: True se foi registro novo (False se foi update)
    if created:
        produto = Produto.objects.get(id=instance.produto_id)
        produto.quantidade = produto.quantidade + instance.quantidade
        produto.save()


def post_save_saida(instance, created, *args, **kwargs):
    # created: True se foi registro novo (False se foi update)
    if created:
        produto = Produto.objects.get(id=instance.produto_id)
        produto.quantidade = produto.quantidade - instance.quantidade
        produto.save()
