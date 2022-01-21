from django.urls import path
from AppCoder2 import views

urlpatterns = [
    path('', views.inicio),
    #path('crearcursos', views.crea_curso),
    path('cursos', views.cursos),
    path('profesores', views.profesores),
    path('estudiantes', views.estudiantes),
    path('entregables', views.entregables),
]
