from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos/json/', views.contatos_json, name='contatos_json'),
    path('contatos/', views.contatos_lista, name='contatos_lista'),
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'),
]