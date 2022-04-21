
from django.urls import path

from .views import home, listaUsuarios

urlpatterns = [
    path('', home,name='index'),
    path('listaUsuarios/',listaUsuarios,name='listaUsuarios')
]