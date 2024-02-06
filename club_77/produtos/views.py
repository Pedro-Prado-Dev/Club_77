from django.shortcuts import render, get_object_or_404
from .models import Produto


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})


def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})


