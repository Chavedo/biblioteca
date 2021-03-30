from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginYStaffUsuarioMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return redirect('index')


class ValidarPermisosRequeridosUsuarioMixin(object):
    permission_required = (
        'usuario.view_usuario', 'usuario.add_usuario', 'usuario.delete_usuario', 'usuario.change_usuario')
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required, str):
            #si el permission_required es un str, return ese permiso..
            #que luego valido con user.has_perms(permiso)
            return (self.permission_required)
        else:
            return(self.permission_required)

    def get_url_redirect(self):
        if self.url_redirect is None:
            # si no hay redireccion, redirecciono para login
            return reverse_lazy('login')
        return self.url_redirect  # redirecciono

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.get_perms()):  # valido en get_perms()
            # si tiene los permisos, continua la ejecucion
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'Permiso denegado.')
        return redirect(self.get_url_redirect())  # si no los tiene
