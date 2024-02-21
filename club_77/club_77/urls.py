"""
URL configuration for club_77 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from produtos import views as produtos_views
from clientes import views as clientes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', produtos_views.lista_produtos, name='lista_produtos'),
    path('detalhes/<int:id>/', produtos_views.detalhes_produto, name='detalhes_produto'),
    path('adicionar/', produtos_views.adicionar_produto, name='adicionar_produto'),
    path('detalhes/<int:produto_id>/', produtos_views.detalhes_produto, name='detalhes_produto'),
    path('editar/<int:produto_id>/', produtos_views.editar_produto, name='editar_produto'),
    path('confirmar_exclusao/<int:produto_id>/', produtos_views.confirmar_exclusao, name='confirmar_exclusao'),
    path('deletar/<int:produto_id>/', produtos_views.deletar_produto, name='deletar_produto'),
    path('clientes/', include('clientes.urls')),
]
