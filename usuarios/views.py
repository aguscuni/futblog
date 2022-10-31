from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Usuarios
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms


# Create your views here.


class ListadoUsuarios(ListView):
    model = Usuarios


class CrearUsuario(TemplateView):
    template_name = "crear.html"
