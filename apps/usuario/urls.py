from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.usuario.views import ListadoUsuario, RegistrarUsuario

urlpatterns = [
    path("listar_usuario/", login_required(ListadoUsuario.as_view()),
         name="listar_usuario"),
    path("crear_usuario/",
         login_required(RegistrarUsuario.as_view()), name="crear_usuario")

]
