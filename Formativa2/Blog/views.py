from django.shortcuts import render
from .models import Publicacion
from .models import Post, Categoria, Etiqueta



# Create your views here.
def base(request,id=None):
    id = request.Get.get('id')
    print (id)
    publicaciones = Post.objects.all().order_by('-fecha').values()

    if id is not None:
        publicacion.actual = Post.objects.get(id = id)


    
def ver_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'ver_publicaciones.html', {'publicaciones' : publicaciones})

    #views para crear publicaciones

#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect
#from .models import Publicacion

#OJO MODIFICACION
def ver_publicaciones(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'ver_publicaciones.html', {'publicaciones': posts})

#ultima publicacion
def post_list(request):
    posts = Post.objects.all()
    latest_post = posts.first()  # Obtener la última publicación

    return render(request, 'ver_publicaciones.html', {'posts': posts, 'latest_post': latest_post})

