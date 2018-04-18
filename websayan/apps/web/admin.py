from django.contrib import admin
from .models import Comunidad, JuntaDirectiva

@admin.register(Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    search_fields = ('titulo',)

@admin.register(JuntaDirectiva)
class JuntaDirectivaAdmin(admin.ModelAdmin):
    pass
