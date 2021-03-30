from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator


class UsuarioManager(BaseUserManager):
    def _create_user(self,username,email,name,last_name,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,email,name,last_name,password = None,**extra_fields):
        return self._create_user(username,email,name,last_name,password,False,False,**extra_fields)

    def create_superuser(self,username,email,name,last_name,password = None,**extra_fields):
        return self._create_user(username,email,name,last_name,password,True,True,**extra_fields) 

class Usuario(AbstractBaseUser, PermissionsMixin):
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
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.username} - {self.name} {self.last_name}'