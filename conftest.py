# pytest busca primero archivos conftest
import pytest

from tests.factories import UsuarioFactory

from apps.usuario.models import Usuario


@pytest.fixture
def user_creation():
    return UsuarioFactory.build()
