from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)


class Publicacion(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    etiquetas = models.ManyToManyField(Etiqueta)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo + "("+ self.autor.first_name + " " + self.autor.last_name + ")"
        
    
#publicacionessss
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
   
            