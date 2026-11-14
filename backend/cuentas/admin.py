from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    ordering = ("email",)
    list_display = ("email", "nombre_visible", "idioma", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "idioma")
    search_fields = ("email", "nombre_visible")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Perfil"), {"fields": ("nombre_visible", "idioma")}),
        (_("Textos legales"), {"fields": ("legal_aceptado_en", "legal_version")}),
        (
            _("Permisos"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        (_("Fechas"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)
