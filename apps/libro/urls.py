
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

urlpatterns = [
    #-- AUTOR --
    path("inicio_autor/", InicioAutor.as_view(), name="inicio_autor"),
    path('crear_autor/',login_required(CrearAutor.as_view()), name = 'crear_autor'),
    path('listar_autor/',login_required(ListadoAutor.as_view()), name = 'listar_autor'),
    path('editar_autor/<int:pk>/',login_required(EditarAutor.as_view()), name = 'editar_autor'),
    path('eliminar_autor/<int:pk>/',login_required(EliminarAutor.as_view()), name = 'eliminar_autor'),
    #-- LIBROS --
    path("inicio_libro/", InicioLibro.as_view(), name="inicio_libro"),
    path('listar_libro/', login_required(ListadoLibros.as_view()), name = 'listar_libro'),
    path('crear_libro/', login_required(CrearLibro.as_view()), name = 'crear_libro'),
    path('editar_libro/<int:pk>/', login_required(EditarLibro.as_view()), name = 'editar_libro'),
    path('eliminar_libro/<int:pk>/', login_required(EliminarLibro.as_view()), name = 'eliminar_libro'),
    #-- USER URLS --
    path('listar-libros-disponibles/',ListadoLibrosUsuarios.as_view(), name = 'listar_libros_disponibles'),
    path('listar-libros-reservados/',ListadoLibrosReservados.as_view(), name = 'listar_libros_reservados'),
    path('detalle-libro/<int:pk>/',DetalleLibroUsuarios.as_view(), name = 'detalle_libro'),
    path('reservar-libro/',RegistrarReserva.as_view(), name = 'reservar_libro')
]


