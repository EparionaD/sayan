from django.shortcuts import render
from django.views.generic import TemplateView
from .models import JuntaDirectiva, Comunidad

class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['juntas'] = JuntaDirectiva.objects.all()
        return context

class LaComunidad(TemplateView):

    template_name = 'comunidad.html'

    def get_context_data(self, **kwargs):
        context = super(LaComunidad, self).get_context_data(**kwargs)
        context['comu'] = Comunidad.objects.all()
        return context
