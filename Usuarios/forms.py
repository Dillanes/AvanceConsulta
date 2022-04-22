from datetime import datetime
from multiprocessing.sharedctypes import Value
from sqlite3 import Date
from this import d
from tkinter.tix import Form
from django import forms
    
TIPO_CONTRATO = ['Planta', 'Temporal', 'Practicas']

class RegistroFrom(forms.Form):
    
    codigo = forms.CharField(label="Codigo", max_length=250, required=True)
    tipocontrato = forms.CharField(label="Tipo de contrato",required=True,max_length=8)
    sueldomensual = forms.FloatField(min_value=400, required=True, label="Sueldo")
    referencia1 = forms.CharField(label="Referencia1",required=True,max_length=8)
    referencia2 = forms.CharField(label="Referencia2",required=True,max_length=8)
    ubicacion = forms.CharField(label="Ubicacion", required=True,max_length=250)
    procedencia = forms.CharField(label="Procedencia",max_length=250,required=True)
    observaciones = forms.CharField(label='Observaciones', widget= forms.Textarea(attrs={'row':5,'cols':20}))