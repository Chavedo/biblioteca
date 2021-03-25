from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .forms import AutorForm
from .models import Autor

"""

Function-based views, not used, were replaced by
Class-based views.

"""

def crear_autor(request):
    # USANDO FORM.PY
    if request.method == 'POST':
        print(request.POST)  # lo que envié
        # los input van a funcionar pq se llaman igual q los field del form eg nombre
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('autor:listar_autor')
    else:
        autor_form = AutorForm()

    return render(request, 'autor/crear_autor.html', {'autor_form': autor_form})


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
        return redirect('autor:listar_autor')
    return render(request, 'autor/crear_autor.html')
'''


def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
    return render(request, 'autor/listar_autor.html', {'autores': autores})


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
            return redirect('/autor/listar_autor/')  # autor:listar_autor

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'autor/crear_autor.html', {'autor_form': autor_form, 'error': error})

# eliminacion directa autor.delete()

def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    # sin verificacion de POST solo autor.deslete()
    if request.method == 'POST':
        autor.estado = False  # eliminacion logica
        autor.save()
        return redirect('autor:listar_autor')
    return render(request, 'autor/eliminar_autor.html', {'autor': autor})
