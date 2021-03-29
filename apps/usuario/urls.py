from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from apps.usuario.views import (EditarUsuario, EliminarUsuario, ListadoUsuario,
                                RegistrarUsuario)

urlpatterns = [

    path("listar_usuario/", login_required(ListadoUsuario.as_view()),
         name="listar_usuario"),
    path("crear_usuario/",
         login_required(RegistrarUsuario.as_view()), name="crear_usuario"),
    path('actualizar_usuario/<int:pk>/',
         login_required(EditarUsuario.as_view()), name='actualizar_usuario'),
    path('eliminar_usuario/<int:pk>/',
         login_required(EliminarUsuario.as_view()), name='eliminar_usuario'),

]

# URLS Implicit views
urlpatterns += [
    path("inicio_usuario/", login_required(
         TemplateView.as_view(
             template_name='usuario/listar_usuario.html'
         )
         ), name="inicio_usuario"),
]
