from django import forms
from .models import Venda
from .models import ItemVenda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'total']


class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        fields = ['produto', 'quantidade']
