from django.shortcuts import render
from django.http import HttpResponse
from AppCoder2.models import Curso
 
# Create your views here.

def curso(self):
    
    curso= Curso(nombre='Desarrollo Web', camada='19881')
    curso.save()
    documentoDeTexto= f'--->Curso: {curso.nombre}    Camada: {curso.camada}'
    
    return HttpResponse(documentoDeTexto)
    