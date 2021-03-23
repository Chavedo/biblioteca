from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'nacionalidad']
        labels = {
            'nombre': 'Nombre del autor',
            'apellido': 'Apellido del autor',
            'nacionalidad': 'Nacionalidad del autor'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del autor',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido del autor',
                    'id': 'apellido'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la nacionalidad del autor',
                    'id': 'nacionalidad'
                }
            )
        }
        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo','autor_id','fecha_publicacion')
        label = {
            'titulo':'Título del libro',
            'autor_id': 'Autor(es) del Libro',
            'fecha_publicacion': 'Fecha de Publciación del Libro'
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese título de libro'
                }
            ),
            'autor_id': forms.SelectMultiple(
                attrs = {
                    'class':'form-control'
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                years=range(1800,2022)
            )
        }