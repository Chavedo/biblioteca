import os
import django,random

os.environ.setdefault("DJANGO_SETTINGS_MODULE","biblioteca.settings")

django.setup()

from faker import Faker
from apps.libro.models import Autor,Libro

#CREACION AUTOR
def autor_create(cant):
    person = Faker(['es_ES','es_MX'])
    for _ in range(cant):
        nuevo_autor = Autor(
            nombre = person.first_name(),
            apellido = person.last_name(),
            nacionalidad = person.country()
        )
        nuevo_autor.save()
        print(nuevo_autor.nombre,nuevo_autor.apellido,nuevo_autor.nacionalidad)
        
    print(f"\nSe crearon {cant} nuevos autores")

def random_id_autor():
    autores = Autor.objects.all().values_list('id',flat=True)
    return random.choice(autores)

#CREACION LIBRO
def libro_create(cant):
    libro = Faker(['en_US'])
    for _ in range(cant):
        nuevo_libro = Libro(  
            titulo = libro.sentence(nb_words=4,variable_nb_words=True ),
            fecha_publicacion = libro.date(pattern='%Y-%m-%d',end_datetime=None),
            descripcion = libro.paragraph(nb_sentences=10),
            imagen = 'libro/book.jpg',
            cantidad = libro.pyint(min_value=1,max_value=3,step=1),
            isbn = libro.isbn10()
        )
        nuevo_libro.save()
        nuevo_libro.autor_id.add(random_id_autor())

        print(nuevo_libro.id,nuevo_libro.titulo,nuevo_libro.fecha_publicacion)

    print(f"\nSe crearon {cant} nuevos autores")

print("Escribe el numero para generar:\n1)Autor\n2)Libro\n")
gen = input()
if gen == "1":
    cant = int(input("Cantidad a generar:"))
    autor_create(cant)
elif gen == "2":
    cant = int(input("Cantidad a generar:"))
    libro_create(cant)
else:
    print("Incorrecto")


