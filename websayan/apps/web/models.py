from django.db import models

class Comunidad(models.Model):

    titulo = models.CharField('Título', max_length=60)
    cuerpo = models.TextField('Descripción')

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'La Comunidad'

    def __str__(self):
        return self.titulo

class JuntaDirectiva(models.Model):

    periodo = models.CharField('Periodo', max_length=60)
    nombre = models.CharField('Nombre', max_length=60)
    cargo = models.CharField('Cargo de la persona', max_length=60)
    foto = models.ImageField('Fotografía', upload_to = 'directiva')

    class Meta:
        ordering  = ['nombre']
        verbose_name_plural = 'Junta Directiva'

    def __str__(self):
        return self.nombre

class GestionAnterior(models.Model):

    cuerpo = models.TextField('Gestiones')

    class Meta:
        verbose_name_plural = 'Gestión Anterior'

    def __str__(self):
        return self.cuerpo

class Desarrollo(models.Model):

    titulo = models.CharField('Título', max_length=60)
    cuerpo = models.TextField('Descripción')

    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Desarrollo'

    def __str__(self):
        return self.titulo