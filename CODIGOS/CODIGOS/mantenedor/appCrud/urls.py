"""appCrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Este es el "directorio" de las rutas generales!!!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('saludos',include('app.urls')),
    path('addCarrera', include('app.urls')),
    path('AgregarCarrera', include('app.urls')),
    path('AgregarAlumno', include('app.urls')),
    path('ListarCarrera', include('app.urls')),
    path('EditarCarrera/<int:carrera_id>', include('app.urls')),
    path('borrar_carrera/<int:carrera_id>', include('app.urls')),
    path('ListarCarreraFull', include('app.urls')),
]
