from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def listaUsuarios(request):
    return render(request,'TablaUsuarios.html')