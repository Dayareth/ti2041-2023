from django.shortcuts import render
from .models import Publicacion


# Create your views here.
def ver_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'ver_publicaciones.html', {'publicaciones' : publicaciones})

    #views para crear publicaciones

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Publicacion

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('ver_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'crear_publicacion.html', {'form': form}) 


#PROFE SI ESTA POR AQUIIII ME ATRAPE :(((AYUDA)))