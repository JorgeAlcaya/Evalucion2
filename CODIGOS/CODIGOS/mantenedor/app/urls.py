from django.urls import path, include
from . import views
#from registration import views

urlpatterns = [
    path('', views.alumnos_list),
    path('saludos', views.pagina_saludos),
    path('addCarrera', views.inscribir_carrera),
    path('AgregarCarrera', views.CarreraCreate.as_view(), name="carrera_crear"),
    path('AgregarAlumno', views.AlumnoCreate.as_view(), name="alumno_crear"),
    path('ListarCarrera', views.listar_carreras),
    path('EditarCarrera/<int:carrera_id>', views.editar_carrera),
    path('borrar_carrera/<int:carrera_id>', views.borrar_carrera),
    path('ListarCarreraFull', views.listar_carreras_full),
]

