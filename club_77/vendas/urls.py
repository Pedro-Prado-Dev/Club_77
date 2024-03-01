from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vendas, name='lista_vendas'),
    path('adicionar/', views.adicionar_venda, name='adicionar_venda'),
    path('detalhes/<int:venda_id>/', views.detalhes_venda, name='detalhes_venda'),
    path('editar/<int:venda_id>/', views.editar_venda, name='editar_venda'),
]