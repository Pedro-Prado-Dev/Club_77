from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('confirmar_exclusao/<int:produto_id>/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
]