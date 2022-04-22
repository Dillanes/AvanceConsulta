from datetime import datetime

from django.shortcuts import render
from .models import Empleados, Usuario
from .forms import RegistroFrom
# Create your views here.

def home(request):
    todosUsuarios = Usuario.objects.all()
    return render(request,'home.html',{'Usuarios':todosUsuarios,})
    
    
def Registrarse(request):
    if request.method == 'POST':
        message2 = Empleados()
        message2.codigo = request.POST.get('codigo')
        message2.fechaing = request.POST.get('fechaingreso')
        message2.fechabaja = request.POST.get('fechabaja')
        message2.tipocontrato = request.POST.get('tipocontrato')
        message2.sueldomensual = request.POST.get('sueldo')
        message2.referencia1 = request.POST.get('referencia1')
        message2.referencia2 = request.POST.get('referencia2')
        message2.ubicacion = request.POST.get('ubicacion')
        message2.procedencia = request.POST.get('procedencia')
        message2.observaciones = request.POST.get('observaciones')
        message2.save()
        
    return render(request,'Registrarse.html',)


def listaUsuarios(request):
    return render(request,'TablaUsuarios.html')