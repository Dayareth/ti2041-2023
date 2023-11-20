from django.shortcuts import render

from .models import Post



# Create your views here.

def base(request):
    post = Post.objects.all().order_by('-fecha')
    return render(request, 'base.html', {'Post': Post})
    
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

