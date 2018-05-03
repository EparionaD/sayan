from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import JuntaDirectiva, Comunidad, GestionAnterior
from .forms import ContactoForm

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

class Junta(TemplateView):

    template_name = 'junta.html'

    def get_context_data(self, **kwargs):
        context = super(Junta, self).get_context_data(**kwargs)
        context['junta'] = JuntaDirectiva.objects.all()
        context['gestion'] = GestionAnterior.objects.all()
        return context

class Contacto(TemplateView):

    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        context = super(Contacto, self).get_context_data(**kwargs)
        context['contacto'] = ContactoForm()
        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        body= render_to_string(
            'contenido_email.html', {
                'nombre': nombre,
                'telefono': telefono,
                'email': email,
                'mensaje': mensaje,
            },
        )

        mensaje_email = EmailMessage(
            subject = 'Mensaje de Usuario',
            body = body,
            from_email = email,
            to = ['eparionad@gmail.com'],
        )

        mensaje_email.content_subtype = 'html'
        mensaje_email.send()

        print(nombre)
        print(telefono)
        print(email)
        print(mensaje)

        return redirect('web:index')
