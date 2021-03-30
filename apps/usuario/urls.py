from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from apps.usuario.views import (InicioUsuario, EditarUsuario, EliminarUsuario, ListadoUsuario,
                                RegistrarUsuario)

urlpatterns = [
    path("inicio_usuario/", InicioUsuario.as_view(), name="inicio_usuario"),
    path("listar_usuario/", ListadoUsuario.as_view(), name="listar_usuario"),
    path("crear_usuario/", RegistrarUsuario.as_view(), name="crear_usuario"),
    path('actualizar_usuario/<int:pk>/',EditarUsuario.as_view(), name='actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/',EliminarUsuario.as_view(), name='eliminar_usuario'),

]