
from django.urls import path

from .views import home, listaUsuarios,Registrarse

urlpatterns = [
    path('', home,name='index'),
    path('listaUsuarios/',listaUsuarios,name='listaUsuarios'),
    path('Registro/',Registrarse,name='Registrarse')
]