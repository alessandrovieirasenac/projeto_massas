from django.contrib import admin
from django.urls import path
from .views import home, login, lista, salvar, delete, editar, update

urlpatterns = [
    path('', home, name = "index"),
    path('login/', login, name = "login"),
    path('lista/', lista, name = "lista"),
    path('salvar/', salvar, name = "salvar"),
    path('apagar/<int:id>', delete, name = "delete"),
    path('editar/<int:id>', editar, name = "editar"),
    path('update/<int:id>', update, name = "update"),
]