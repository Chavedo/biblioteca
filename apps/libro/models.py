from django.db import models


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellido = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField(
        'Fecha creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return (self.nombre + ' ' + self.apellido)

    class Meta:
        ordering = ['id']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


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
