from django.urls import path
from . import views

app_name = 'página_principal'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    # Adicione outras URLs conforme necessário para conectar a outras listas
]