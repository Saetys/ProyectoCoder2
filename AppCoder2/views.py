from django.shortcuts import render
from django.http import HttpResponse
from AppCoder2.models import Curso, Profesor
from AppCoder2.forms import CursoFormulario, ProfesoresFormulario
 
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
     
    if(request.method == 'POST'):
        
        miFormulario= CursoFormulario(request.POST)
    
        print(miFormulario)
        
        if(miFormulario.is_valid()):
            
            informacion= miFormulario.cleaned_data
    
            curso= Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
        
            return render(request, 'AppCoder2/inicio.html')
    
    else:
        
        miFormulario= CursoFormulario()
    
    return render(request, 'AppCoder2/cursoFormulario.html', {'miFormulario':miFormulario})


def profesoresFormulario(request):
    
    if(request.method == 'POST'):
        
        miFormulario= ProfesoresFormulario(request.POST)
    
        print(miFormulario)
        
        if(miFormulario.is_valid()):
            
            informacion= miFormulario.cleaned_data
    
            profesor= Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], 
             email=informacion["email"], profesion=informacion["profesion"])
            profesor.save()
        
            return render(request, 'AppCoder2/inicio.html')
    
    else:
        
        miFormulario= ProfesoresFormulario()
    
    return render(request, 'AppCoder2/profesoresFormulario.html', {'miFormulario':miFormulario})


def busquedaCamada(request):
    
    return render(request, 'AppCoder2/busquedaCamada.html')

def buscar(request):
    
    if (request.method == 'GET'):
        
        camada= request.GET["camada"]
        cursos= Curso.objects.filter(camada=camada)
        
        return render(request, 'AppCoder2/resultadosBusqueda.html', {"cursos": cursos, "camada": camada})
    
    else:
        
        return HttpResponse('No enviaste datos')

    