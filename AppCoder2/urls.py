from django.urls import path
from AppCoder2 import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    #path('crearcursos', views.crea_curso),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('cursoFormulario/', views.cursoFormulario, name="CursoFormulario"),
    path('profesoresFormulario/', views.profesoresFormulario, name="ProfesoresFormulario"),
    path('busquedaCamada/', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar, name="Buscar"),
]
