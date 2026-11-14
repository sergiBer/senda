"""Usuario de Senda (modelo de datos §4.4).

Email como identificador, compatible con allauth. Sin perfil de familia ni
edades de hijos (EDA-02, COM-07).
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Un superusuario necesita is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Un superusuario necesita is_superuser=True")
        return self._create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
    class Idioma(models.TextChoices):
        ES = "es", "Español"
        CA = "ca", "Català"
        EN = "en", "English"

    username = None
    first_name = None
    last_name = None

    email = models.EmailField(_("email"), unique=True)
    nombre_visible = models.CharField(_("nombre visible"), max_length=60, blank=True)
    idioma = models.CharField(_("idioma"), max_length=2, choices=Idioma.choices, default=Idioma.ES)
    legal_aceptado_en = models.DateTimeField(
        _("textos legales aceptados en"), null=True, blank=True
    )
    legal_version = models.CharField(_("versión de los textos legales"), max_length=20, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = _("usuario")
        verbose_name_plural = _("usuarios")

    def __str__(self):
        return self.email
