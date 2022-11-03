from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import DetallesBlog
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.


class MostrarDetallesBlog(ListView):
    model = DetallesBlog

class EditarDetallesBlog(SuccessMessageMixin, UpdateView):
    model = DetallesBlog
    form = DetallesBlog
    fields = "__all__"
    success_message = "Detalle(s) editado(s) correctamente!"

    def get_success_url(self):
        return reverse("detallesblog")
