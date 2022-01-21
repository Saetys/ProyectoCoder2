from django.shortcuts import render
from django.http import HttpResponse
from AppCoder2.models import Curso
 
# Create your views here.

#def crea_curso(self):
    
 #   curso= Curso(nombre='Desarrollo Web', camada='19881')
  #  curso.save()
   # documentoDeTexto= f'--->Curso: {curso.nombre}    Camada: {curso.camada}'
    
    #return HttpResponse(documentoDeTexto)

def inicio(request):
    
    return render(request, 'AppCoder2/inicio.html')

def cursos(request):
    
    return render(request, 'AppCoder2/cursos.html')

def profesores(request):
    
    return render(request, 'AppCoder2/profesores.html')

def estudiantes(request):
    
    return render(request, 'AppCoder2/estudiantes.html')

def entregables(request):
    
    return render(request, 'AppCoder2/entregables.html')    