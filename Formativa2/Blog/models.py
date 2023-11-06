from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    etiquetas = models.ManyToManyField(Etiqueta)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
