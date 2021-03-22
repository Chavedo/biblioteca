from django import forms
from .models import Autor


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
