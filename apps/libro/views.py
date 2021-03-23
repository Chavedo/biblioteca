from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


class Inicio(TemplateView):
    template_name = "index.html"


class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)

    

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = "libro/autor/crear_autor.html"
    form_class = AutorForm
    success_url = reverse_lazy('autor:listar_autor')


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('autor:listar_autor')


class EliminarAutor(DeleteView):
    model = Autor
    #logic delete
    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('autor:listar_autor')


class ListadoLibros(ListView):
    model = Libro
    template_name = 'libro/libro/listar_libro.html' # queryset = Libro.objects.all()
    queryset = Libro.objects.filter(estado = True)

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listado_libros')

class EliminarLibro(DeleteView):
    model = Libro

    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listado_libros')