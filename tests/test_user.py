import pytest

from apps.usuario.models import Usuario

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
