from django.contrib.auth import login, logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from apps.usuario.models import Usuario

from .forms import FormularioLogin, FormularioUsuario


class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    # adds CSRF protection,it can be used on a per view basis
    @method_decorator(csrf_protect)
    # adds headers to a response so that it will never be cached
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuario.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuario:listar_usuario')
