from django.core.serializers import serialize
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View, DetailView)

from apps.libro.mixins import LoginMixin
from apps.libro.models import Autor, Libro, Reserva
from apps.usuario.models import Usuario

from .forms import AutorForm, LibroForm


class InicioAutor(TemplateView):

    template_name = "libro/autor/listar_autor.html"


class ListadoAutor(ListView):

    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/listar_autor.html'

    def get_queryset(self):

        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = {}
        context['autores'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('libro:inicio_autor')


class CrearAutor(CreateView):
    """
    View for creating a new object, with a response rendered by a template.
    """
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_autor = Autor(
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido'),
                    nacionalidad=form.cleaned_data.get('nacionalidad')
                )
                nuevo_autor.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse(
                    {'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('libro:inicio_autor')


class EditarAutor(UpdateView):
    """
    View for updating an object, with a response rendered by a template.
    """
    model = Autor
    form_class = AutorForm
    template_name = "libro/autor/editar_autor.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('libro:inicio_autor')


class EliminarAutor(DeleteView):

    """
    Logic elimination of author, only the state is changed to false.
    It doesn't elminate it from db
    """

    model = Autor
    template_name = 'libro/autor/eliminar_autor.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            autor = self.get_object()
            autor.estado = False
            autor.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('libro:inicio_autor')


class InicioLibro(TemplateView):

    template_name = "libro/libro/listar_libro.html"


class ListadoLibros(ListView):

    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html'

    def get_queryset(self):

        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        """
        Returns a dictionary representing the template context.
        The keyword arguments provided will make up the returned context. 
        """
        context = {}
        context['libros'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('libro:inicio_libro')


class CrearLibro(CreateView):
    # create book
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(
                data=request.POST, files=request.FILES, instance=self.get_object())
            if form.is_valid():
                nuevo_libro = Autor(
                    titulo=form.cleaned_data.get('titulo'),
                    fecha_publicacion=form.cleaned_data.get(
                        'fecha_publicacion'),
                    autor_id=form.cleaned_data.get('autor_id'),

                )
                nuevo_libro.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse(
                    {'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('libro:inicio_libro')


class EditarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/editar_libro.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha podido actualizar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('libro:inicio_libro')


class EliminarLibro(DeleteView):
    model = Libro
    template_name = 'libro/libro/eliminar_libro.html'

    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            libro = self.get_object()
            libro.estado = False
            libro.save()
            mensaje = f'{self.model.__name__} eliminado correctamente!'
            error = 'No hay error!'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('libro:inicio_autor')


class ListadoLibrosUsuarios(LoginMixin, ListView):
    model = Libro
    paginate_by = 6
    template_name = 'libro/libros_disponibles.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(
            estado=True, cantidad__gte=1)  # <=
        return queryset


class DetalleLibroUsuarios(LoginMixin, DetailView):
    model = Libro
    template_name = 'libro/detalle_libro_disponible.html'


class RegistrarReserva(LoginMixin, CreateView):
    model = Reserva
    success_url = reverse_lazy('libro:listar_libros_reservados')

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            libro = Libro.objects.filter(id=request.POST.get('libro')).first()
            usuario = Usuario.objects.filter(
                id=request.POST.get('usuario')).first()
            if libro:
                nueva_reserva = self.model(
                    libro=libro,
                    usuario=usuario
                )
                nueva_reserva.save()
                mensaje = f'{self.model.__name__} registrado correctamente!'
                error = 'No hay error!'
                response = JsonResponse({'mensaje':mensaje,'error':error,'url':self.success_url})
                response.status_code = 201
                return response
            return redirect('libro:listar_libros_disponibles')

class ListadoLibrosReservados(LoginMixin,ListView):
    model = Reserva
    paginate_by = 6
    template_name = 'libro/libros_reservados.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(estado=True,usuario=self.request.user.id)
        return queryset
