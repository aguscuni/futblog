from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categorias
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


# Create your views here.


class ListadoCategorias(ListView):
    model = Categorias


class CrearCategoria(SuccessMessageMixin, CreateView):
    model = Categorias
    form = Categorias
    fields = "__all__"
    success_message = "Categoría creada correctamente!"

    def get_success_url(self):
        return reverse("listadodecategorias")

class EditarCategoria(SuccessMessageMixin, UpdateView):
    model = Categorias
    form = Categorias
    fields = "__all__"
    success_message = "Categoría editada correctamente!"

    def get_success_url(self):
        return reverse("listadodecategorias")

class EliminarCategoria(SuccessMessageMixin, DeleteView):
    model = Categorias
    form = Categorias
    fields = "__all__"

    def get_success_url(self):
        success_message = "Categoría eliminada correctamente!"
        messages.success(self.request, (success_message))
        return reverse("listadodecategorias")
