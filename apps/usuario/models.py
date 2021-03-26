from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class UsuarioManager(BaseUserManager):
    def create_user(self,  email, username, name, last_name, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            last_name=last_name,
            
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, name, last_name, password):
        usuario = self.create_user(
            email,
            username=username,
            name=name,
            last_name=last_name,
            password=password
        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    username = models.IntegerField(
        'Legajo usuario', unique=True, validators=[MaxValueValidator(99999), MinValueValidator(1)])
    email = models.EmailField('Email de usuario', max_length=254)
    name = models.CharField('Nombre', blank=True, max_length=50, null=True)
    last_name = models.CharField(
        'Apellido', blank=True, max_length=50, null=True)
    date_of_birth = models.DateField(
        'Fecha nacimiento', null=True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/',
                              height_field=None, width_field=None, max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.username} - {self.name} {self.last_name}'

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
