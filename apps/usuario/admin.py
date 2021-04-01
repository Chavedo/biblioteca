from apps.usuario.models import Usuario
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Usuario

admin.site.register(Usuario)
admin.site.register(Permission)
#consulto el contenido de un modelo para desp hacer permisos
admin.site.register(ContentType)