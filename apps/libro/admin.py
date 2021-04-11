from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Autor, Libro, Reserva
from .forms import ReservaForm

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor
        
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('nombre','apellido','nacionalidad')
    list_display = ('nombre','apellido','nacionalidad','estado')
    resource_class = AutorResource
    actions = ['eliminacion_logica_autores', 'activacion_logica_autores']

    def eliminacion_logica_autores(self, request, queryset):
        for autor in queryset:
            autor.estado = False
            autor.save()

    def activacion_logica_autores(self, request, queryset):
        for autor in queryset:
            autor.estado = True
            autor.save()

    #quitar opcion por defecto de django
    def get_actions(self,request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro

class LibroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','get_autor_id','fecha_publicacion','estado')
    resource_class = LibroResource
    actions = ['eliminacion_logica_libro', 'activacion_logica_libro']


    def eliminacion_logica_libro(self, request, queryset):
        for libro in queryset:
            libro.estado = False
            libro.save()

    def activacion_logica_libro(self, request, queryset):
        for libro in queryset:
            libro.estado = True
            libro.save()

class ReservaAdmin(admin.ModelAdmin):
    form = ReservaForm
    list_display = ('libro','usuario','fecha_creacion','estado')
    

admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Reserva, ReservaAdmin)
