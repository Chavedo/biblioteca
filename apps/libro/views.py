from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = "index.html"


class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)

    

class AcualizarAutor(UpdateView):
    model = Autor
    template_name = "libro/crear_autor.html"
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')


class EliminarAutor(DeleteView):
    model = Autor
    #logic delete
    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')


def crear_autor(request):
    # USANDO FORM.PY
    if request.method == 'POST':
        print(request.POST)  # lo que envié
        # los input van a funcionar pq se llaman igual q los field del form eg nombre
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('libro:listar_autor')
    else:
        autor_form = AutorForm()

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})


# crear autor sin usar forms.py
'''def crear_autor(request):
    #SIN USAR FORM
    if request.method == 'POST':
        print(request.POST) #lo que envié
        nom = request.POST.get('nombre')
        ape = request.POST.get('apellido')
        nac = request.POST.get('nacionalidad')
        autor = Autor(nombre = nom, apellido=ape,nacionalidad=nac)
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/crear_autor.html')
'''


def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('/libro/listar_autor/')  # libro:listar_autor

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'error': error})

# eliminacion directa autor.delete()

def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    # sin verificacion de POST solo autor.deslete()
    if request.method == 'POST':
        autor.estado = False  # eliminacion logica
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})
