import pytest
from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError, connection


def test_el_modelo_de_usuario_es_cuentas_usuario():
    assert get_user_model()._meta.label == "cuentas.Usuario"


@pytest.mark.django_db
def test_crear_usuario_con_email_sin_username():
    # Dado un email y una contraseña
    # Cuando se crea un usuario
    usuario = get_user_model().objects.create_user(email="Ana@Example.com", password="s3nda-pass")
    # Entonces se identifica por email (dominio normalizado), sin username, idioma es por defecto
    assert usuario.email == "Ana@example.com"
    assert usuario.username is None
    assert usuario.idioma == "es"
    assert authenticate(email="Ana@example.com", password="s3nda-pass") == usuario


@pytest.mark.django_db
def test_el_email_es_unico():
    modelo = get_user_model()
    modelo.objects.create_user(email="ana@example.com", password="x")
    with pytest.raises(IntegrityError):
        modelo.objects.create_user(email="ana@example.com", password="y")


@pytest.mark.django_db
def test_crear_superusuario():
    admin = get_user_model().objects.create_superuser(email="admin@example.com", password="x")
    assert admin.is_staff and admin.is_superuser


@pytest.mark.django_db
def test_postgis_disponible():
    with connection.cursor() as cursor:
        cursor.execute("SELECT PostGIS_Version()")
        assert cursor.fetchone()[0]
