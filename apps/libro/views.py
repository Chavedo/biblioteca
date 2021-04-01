from django.core.serializers import serialize
from django.http import response
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View)

from .forms import AutorForm, LibroForm
from .models import Autor, Libro

class InicioAutor(TemplateView):
    
    template_name = "libro/autor/listar_autor.html"

class ListadoAutor(ListView):
    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    """
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
            return redirect('libro:listar_autor')


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
            return redirect('libro:listar_autor')


class EliminarAutor(DeleteView):

    """
    Logic elimination of author, only the state is changed to false.
    It doesn't elminate it from db
    """

    model = Autor

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
            return redirect('libro:listar_autor')


class CrearLibro(CreateView):
    # create book
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')


class ListadoLibros(View):
    """
    Intentionally simple parent class for all views. Only implements
    dispatch-by-method and simple sanity checking.
    """
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
        return render(request, self.template_name, self.get_context_data())


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libros"] = Libro.objects.filter(estado=True)
        return context


class EliminarLibro(DeleteView):
    model = Libro

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id=pk)  # primary key
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')
