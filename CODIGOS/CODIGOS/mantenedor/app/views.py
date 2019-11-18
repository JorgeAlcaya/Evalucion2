from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django import forms
# Importamos las estructuras solicitadas
from .models import Carrera, Alumno
from .forms import CarreraForm, AlumnoForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView


# Create your views here.


def alumnos_list(request):
    return render(request, 'app/alumnos_list.html', {})


def pagina_saludos(request):
    return render(request, 'app/saludos.html', {})

# -- Creamos una función para agregar carrera --


def inscribir_carrera(request):
    if request.method == "POST":
        form = CarreraForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = CarreraForm()
        return render(request, 'app/ins_carrera.html', {'form': form})


def inscribir_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if(form.is_valid):
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/')
    else:
        form = AlumnoForm()
        return render(request, 'app/agregar_alumno.html', {'form': form})


def listar_carreras(request):
    # creamos una variable que sera coleccion y carga TODOS los registros
    carreras = Carrera.objects.all()
    # renderizamos la coleccion  en el template: listar_carreras.html
    return render(request, "app/listar_carreras.html", {'carreras': carreras})

def listar_carreras_full(request):
    # creamos una variable que sera coleccion y carga TODOS los registros
    carreras = Carrera.objects.all()
    # renderizamos la coleccion  en el template: listar_carreras.html
    return render(request, "app/listar_carreras_full.html", {'carreras': carreras})

def editar_carrera(request, carrera_id):
    # Recuperamos el objeto asociado a id
    instancia = Carrera.objects.get(id=carrera_id)
    # creamos un formulario que contenga los fdatos del registro recuperado
    form = CarreraForm(instance=instancia)

    # Comprobamos que sea enviado el formulario
    if request.method == "POST":
        form = CarreraForm(request.POST, instance=instancia)
        if form.is_valid():
            instance = form.save(commit=False)
            instancia.save()

    return render(request, "app/editar_carrera.html", {'form': form})

def borrar_carrera(request, carrera_id):
     instancia = Carrera.objects.get(id=carrera_id)
     instancia.delete()   
     return redirect("/") #--> al raiz de las paginas 



# Otra Forma es usar las clases generics de Django
class CarreraCreate(CreateView):
    model = Carrera
    form_class = CarreraForm
    templates_name = 'app/ins_carrera.html'
    success_url = reverse_lazy('carrera_crear')


class AlumnoCreate(CreateView):
    model = Alumno
    form_class = AlumnoForm
    templates_name = 'app/alumno_agregar.html'
    success_url = reverse_lazy('alumno_crear')


