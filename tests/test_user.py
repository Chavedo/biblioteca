from django.http import response
import pytest

from django.test import TestCase, Client

from apps.usuario.models import Usuario
from tests.factories import UsuarioFactory, UsuarioAdminFactory

"""
@pytest.mark.django_db
def test_common_user_creation(user_creation):
    print(user_creation.email)
    assert user_creation.is_staff == False


@pytest.mark.django_db
def test_superuser_creation(user_creation):
    user_creation.is_superuser = True
    user_creation.is_staff = True
    assert user_creation.is_superuser


@pytest.mark.django_db
def test_staff_creation():
    user = Usuario.objects.create_user(
        username='12121',
        email='asd@gmail.com',
        name='Carlos',
        last_name='Pincha',
        is_staff=True,
        password='12345'
    )
    assert user.is_staff


@pytest.mark.django_db
def test_user_creation_fail():
    with pytest.raises(Exception):
        Usuario.objects.create_user(
            password='12345',
            is_staff=False
        )
"""


class UsuarioTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.common_user = UsuarioFactory.create()
        self.superuser = UsuarioAdminFactory.create()

    def test_common_user_creation(self):
        self.assertEqual(self.common_user.is_active, True)
        self.assertEqual(self.common_user.is_staff, False)
        self.assertEqual(self.common_user.is_superuser, False)

    def test_superuser_creation(self):
        self.assertEqual(self.superuser.is_staff, True)

    def test_login(self):
        self.common_user.set_password('qweasd')
        self.common_user.save()
        response = self.client.login(username='42966', password='qweasd')
        self.assertEqual(response, True)

    def test_login_fail(self):
        self.common_user.set_password('qweasd')
        self.common_user.save()
        response = self.client.login(username='42966', password='qweasd2')
        self.assertEqual(response, False)

    def test_user_list(self):
        self.superuser.set_password('qweasd')
        self.superuser.save()
        self.client.login(username='12345', password='qweasd')
        response = self.client.get(
            '/usuario/listar_usuario/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
