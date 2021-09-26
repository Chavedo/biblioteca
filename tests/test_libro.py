import pytest

from ddf import G, F
from faker import Faker

from apps.libro.models import Autor, Libro

faker = Faker()

@pytest.fixture
def create_libro():
    # forma 1
    autores = [F(nombre=faker.last_name()) for i in range(3)]
    return G(Libro, autor_id=autores)

    # forma 2 combinada
    # autor_1 = G(Autor)
    # autor_2 = G(Autor)
    # return G(Libro, autor_id=[autor_1, autor_2, F()])

@pytest.mark.django_db
def test_create_libro(create_libro):
    print(create_libro.autor_id.all())
    assert create_libro.estado
