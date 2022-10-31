from django.db import models

from django.utils import timezone

# Create your models here.


class Entradas(models.Model):
    titulo = models.CharField(max_length=5000, default="DEFAULT VALUE")
    contenido = models.TextField(default="DEFAULT VALUE")
    imagen_destacada = models.FileField()
    slug = models.CharField(max_length=5000, default="DEFAULT VALUE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "entradas"
