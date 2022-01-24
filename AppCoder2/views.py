from django.shortcuts import render
from django.http import HttpResponse
from AppCoder2.models import Curso
 
# Create your views here.

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

def cursoFormulario(request):
    
    print(request.POST)
    
    if(request.method == 'POST'):
    
        curso= Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
        curso.save()
        
        return render(request, 'AppCoder2/inicio.html')
    
    return render(request, 'AppCoder2/cursoFormulario.html')