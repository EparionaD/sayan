from django.shortcuts import render
from django.views.generic import TemplateView
from .models import JuntaDirectiva

class Index(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['juntas'] = JuntaDirectiva.objects.all()
        return context