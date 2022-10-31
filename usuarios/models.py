from django.db import models

from django.utils import timezone

# Create your models here.


class Usuarios(models.Model):
    nombre = models.CharField(max_length=500, default="DEFAULT VALUE")
    foto_perfil = models.FileField()
    pagina_web = models.CharField(max_length=1000, default="DEFAULT VALUE")
    descripcion = models.TextField(default="DEFAULT VALUE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "usuarios"
