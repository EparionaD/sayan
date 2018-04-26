from django.contrib import admin
from .models import Comunidad, JuntaDirectiva, Desarrollo, GestionAnterior

@admin.register(Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    search_fields = ('titulo',)

@admin.register(JuntaDirectiva)
class JuntaDirectivaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

@admin.register(Desarrollo)
class DesarrolloAdmin(admin.ModelAdmin):
    search_fields = ('titulo',)

@admin.register(GestionAnterior)
class GestionAnteriorAdmin(admin.ModelAdmin):
    pass
