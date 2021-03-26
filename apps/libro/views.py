from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView, View)

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


class Inicio(TemplateView):
    """
    Render a template. Pass keyword arguments from the URLconf to the context.
    """
    template_name = "index.html"


class CrearAutor(CreateView):
    """
    View for creating a new object, with a response rendered by a template.
    """
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')


class ListadoAutor(View):
    """
    Render some list of objects, set by `self.model` or `self.queryset`.
    `self.queryset` can actually be any iterable of items, not just a queryset.
    """
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/listar_autor.html'

    def get_queryset(self):

        return self.model.objects.filter(estado=True)

    def get_context_data(self):
        context = {}
        context['autores'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class ActualizarAutor(UpdateView):
    """
    View for updating an object, with a response rendered by a template.
    """
    model = Autor
    template_name = "libro/autor/autor.html"
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class EliminarAutor(DeleteView):
    model = Autor
    """
    Logic elimination of author, only the state is changed to false.
    It doesn't elminate it from db
    """
    def post(pk):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('autor:listar_autor')


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

    def get_context_data(self):
        """
        Returns a dictionary representing the template context.
        The keyword arguments provided will make up the returned context. 
        """
        context = {}
        context['libros'] = self.get_queryset()
        context['form'] = self.form_class
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/libro.html'
    success_url = reverse_lazy('libro:listado_libros')

    def get_context_data(**kwargs):
        context = super().get_context_data(**kwargs)
        context["libros"] = Libro.objects.filter(estado=True)
        return context


class EliminarLibro(DeleteView):
    model = Libro

    def post(pk):
        object = Libro.objects.get(id=pk)  # primary key
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')
