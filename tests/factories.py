import factory
from faker import Faker

from apps.usuario.models import Usuario
from tests.providers.general_providers import EmailProvider, UsernameProvider


fake = Faker()
fake.add_provider(EmailProvider)
fake.add_provider(UsernameProvider)


class UsuarioFactory(factory.Factory):
    class Meta:
        model = Usuario

    name = 'mariano'
    username = '42966'
    email = fake.email()
    is_staff = False


class UsuarioAdminFactory(factory.Factory):
    class Meta:
        model = Usuario

    name = 'Oliver'
    username = '12345'
    is_staff = True
    is_superuser = True


class UsuarioStaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Usuario

    name = fake.name()
    username = fake.username()
    email = fake.email()
    is_staff = True
