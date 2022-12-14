"""blogfutbol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from categorias.views import ListadoCategorias, CrearCategoria, EditarCategoria, EliminarCategoria
from detallesblog.views import MostrarDetallesBlog, EditarDetallesBlog
from entradas.views import ListadoEntradas, CrearEntrada
from usuarios.views import ListadoUsuarios, CrearUsuario

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("categorias/", ListadoCategorias.as_view(template_name="categorias/index.html"), name="listadodecategorias"),
    path("categorias/crear", CrearCategoria.as_view(template_name="categorias/crear.html"), name="crearcategoria"),
    path("categorias/editar/<int:pk>", EditarCategoria.as_view(template_name="categorias/editar.html"), name="editarcategoria"),
    path("categorias/eliminar/<int:pk>", EliminarCategoria.as_view(), name="eliminarcategoria"),
    path("detallesblog/", MostrarDetallesBlog.as_view(template_name="detallesblog/index.html"), name="detallesblog"),
    path("detallesblog/editar/<int:pk>", EditarDetallesBlog.as_view(template_name="detallesblog/editar.html"), name="editardetalles"),
    path("entradas/", ListadoEntradas.as_view(template_name="entradas/index.html"), name="listadodeentradas"),
    path("entradas/crear", CrearEntrada.as_view(template_name="entradas/crear.html"), name="crearentrada"),
    path("usuarios/", ListadoUsuarios.as_view(template_name="usuarios/index.html"), name="listadodeusuarios"),
    path("usuarios/crear", CrearUsuario.as_view(template_name="usuarios/crear.html"), name="crearusuario"),
]
