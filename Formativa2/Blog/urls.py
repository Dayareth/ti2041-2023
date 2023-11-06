from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_publicaciones, name='ver_publicaciones'),
    path('publicar/', views.crear_publicacion, name='crear_publicacion'),
    
]