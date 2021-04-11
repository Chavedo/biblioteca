from django.db import models
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.signals import post_save, pre_save
from apps.usuario.models import Usuario


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

    # para usar con use_natural_foreign_keys=True), muestra el return en vez de id
    def natural_key(self):
        return (self.nombre + ' ' + self.apellido)


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(
        'Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField(
        'Fecha de publicacion', blank=False, null=False)
    descripcion = TextField('Descripción', null=True, blank=True)
    cantidad = models.PositiveIntegerField('Stock', default=1)
    imagen = models.ImageField(
        'Imagen', upload_to='libro/', max_length=255, null=True, blank=True)
    autor_id = models.ManyToManyField(Autor)
    isbn = models.CharField('ISBN', blank=True, null=True, max_length=50)
    fecha_creacion = models.DateField(
        'Fecha creacion', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    # OBTENGO EL STR DE LOS AUTORES DEL LIBRO, PROBLEMAS CON M2M EN LIST_DISPLAY ADMIN.PY
    def get_autor_id(self):
        return "\n".join([p.__str__() for p in self.autor_id.all()])

    #funcion del pibe- no la uso nunca
    def obtener_autores(self):
        autores = str([autor for autor in self.autor_id.all().values_list('nombre',flat=True)])
        autores = autores.replace("[","").replace("]","").replace("'","")
        return autores

    def natural_key(self):
        return f'{self.titulo} - {self.get_autor_id()}'

def quitar_autor_libro(sender, instance, **kwargs):
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


# enlaze de la funcion con el post_save
post_save.connect(quitar_autor_libro, sender=Autor)


class Reserva(models.Model):
    """Model definition for Reserva

    Args:
        models ([type]): [description]
    """
    id = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    cantidad_dias = models.SmallIntegerField(
        'Cantidad dias a reservar', default=7)
    fecha_creacion = models.DateField(
        'Fecha de creación', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(default=True, verbose_name='Estado')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva de {self.libro} por {self.usuario}'

def reducir_cantidad_libro(sender,instance,**kwargs):
    libro = instance.libro
    if libro.cantidad > 0:
        libro.cantidad = libro.cantidad - 1
        libro.save()

def validar_creacion_reserva(sender,instance,**kwargs):
    libro = instance.libro
    if libro.cantidad < 1:
        raise Exception('No se puedo realizar la reservar')

post_save.connect(reducir_cantidad_libro,sender = Reserva)
#pre_save.connect(validar_creacion_reserva,sender = Reserva)