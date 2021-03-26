from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import fields
from django.forms import widgets
from apps.usuario.models import Usuario

# this form is preferable


class FormularioLogin(AuthenticationForm):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Legajo'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    """ Formulario de registro de un usuario en la base de datos

    Variables:

        -passoword: Contraseña
        -password2: Verificacion de la contraseña
    """
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese la contraseña...',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Confirmacion de contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente la contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = {'username', 'email', 'name', 'last_name'}
        widgets = {
            'username': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Legajo'
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }
            ),
        }

    def clean_password2(self):
        # validation password method
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user