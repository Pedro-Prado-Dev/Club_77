from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from .forms import VendaForm, ItemVendaForm
from .models import Venda, ItemVenda


def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/lista_vendas.html', {'vendas': vendas})


def adicionar_venda(request):
    if request.method == 'POST':
        venda_form = VendaForm(request.POST)
        item_form = ItemVendaForm(request.POST)
        if venda_form.is_valid() and item_form.is_valid():
            venda = venda_form.save()
            item = item_form.save(commit=False)
            item.venda = venda
            item.save()
            return redirect('lista_vendas')
    else:
        venda_form = VendaForm()
        item_form = ItemVendaForm()
    return render(request, 'vendas/adicionar_venda.html', {'venda_form': venda_form, 'item_form': item_form})

def detalhes_venda(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    return render(request, 'vendas/detalhes_venda.html', {'venda': venda})


def editar_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    if request.method == 'POST':
        venda_form = VendaForm(request.POST, instance=venda, prefix='venda')
        if venda_form.is_valid():
            with transaction.atomic():
                venda = venda_form.save()

                # Atualizar o estoque de cada item de venda
                for item in venda.itemvenda_set.all():
                    produto = item.produto
                    quantidade_vendida_anterior = item.quantidade

                    # Reverter o estoque do produto para o valor anterior
                    produto.quantidade += quantidade_vendida_anterior
                    produto.save()

                    # Atualizar o estoque do produto de acordo com a nova quantidade
                    quantidade_vendida_nova = request.POST.get(f'item_venda_{item.id}-quantidade')
                    produto.quantidade -= int(quantidade_vendida_nova)
                    produto.save()

            return redirect('lista_vendas')
    else:
        venda_form = VendaForm(instance=venda, prefix='venda')

        itens_venda = ItemVenda.objects.filter(venda=venda)
        item_venda_forms = [ItemVendaForm(instance=item, prefix=f'item_venda_{item.id}') for item in itens_venda]
    return render(request, 'vendas/editar_venda.html', {'venda_form': venda_form, 'item_venda_forms': item_venda_forms, 'venda': venda})