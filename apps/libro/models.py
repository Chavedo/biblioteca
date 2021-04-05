from django.db import models
from django.db.models.signals import post_save


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellido = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField(
        'Fecha creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default=True)


    class Meta:
        ordering = ['nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return (self.nombre + ' ' + self.apellido)    

    #para usar con use_natural_foreign_keys=True), muestra el return en vez de id
    def natural_key(self):
        return (self.nombre + ' ' + self.apellido)

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField(
        'Fecha de publicacion', blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField(
        'Fecha creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(default = True, verbose_name = 'Estado')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    #OBTENGO EL STR DE LOS AUTORES DEL LIBRO, PROBLEMAS CON M2M EN LIST_DISPLAY ADMIN.PY
    def get_autor_id(self):
        return "\n".join([p.__str__() for p in self.autor_id.all()])

def quitar_autor_libro(sender,instance,**kwargs):
    """Cuando elimino un autor, cambio el estado de los libros a false

    Args:
        sender (model): modelo a enlazar
        instance ([type]): [description]
    """
    if instance.estado == False:
        autor = instance.id
        libros = Libro.objects.filter(autor_id=autor)
        for libro in libros:
            libro.estado = False
            libro.save()
        

#enlaze de la funcion con el post_save
post_save.connect(quitar_autor_libro,sender = Autor)