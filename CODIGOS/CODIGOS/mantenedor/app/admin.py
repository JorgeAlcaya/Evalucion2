from django.contrib import admin
from .models import Alumno, Carrera
# Register your models here.

admin.site.register(Carrera)
admin.site.register(Alumno)
