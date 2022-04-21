from django.shortcuts import render
from .models import Omc23Nivel1
# Create your views here.

def home(request):
    todoE = Omc23Nivel1.objects.all()
    return render(request,'home.html',{'Empleados':todoE})

def listaUsuarios(request):
    return render(request,'TablaUsuarios.html')