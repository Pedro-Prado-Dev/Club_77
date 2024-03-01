from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ItemVenda

@receiver(post_save, sender=ItemVenda)
def atualizar_estoque(sender, instance, **kwargs):
    produto = instance.produto
    quantidade_vendida = instance.quantidade
    produto.estoque -= quantidade_vendida
    produto.save()