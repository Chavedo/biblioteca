from apps.usuario.models import Usuario
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('username','name','last_name')
    list_display = ('username', 'name', 'last_name', 'is_active', 'is_staff')
    actions = ['eliminacion_logica_usuario','activacion_logica_usuario']

    def eliminacion_logica_usuario(self, request, queryset):
        queryset = queryset.exclude(is_staff=True)
        for usuario in queryset:
            usuario.is_active = False
            usuario.save()

    def activacion_logica_usuario(self, request, queryset):
        queryset = queryset.exclude(is_staff=True)
        for usuario in queryset:
            usuario.is_active = True
            usuario.save()


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Permission)
# consulto el contenido de un modelo para desp hacer permisos
admin.site.register(ContentType)
