from django.shortcuts import render
from .models import Empleados, Usuario

# Create your views here.

def home(request):
    
    todosUsuarios = Usuario.objects.all()
    return render(request,'home.html',{'Usuarios':todosUsuarios})



def listaUsuarios(request):
    return render(request,'TablaUsuarios.html')