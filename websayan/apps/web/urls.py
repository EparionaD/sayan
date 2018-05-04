from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name = 'index'),
    url(r'^comunidad/', views.LaComunidad.as_view(), name = 'comunidad'),
    url(r'^junta-directiva/', views.Junta.as_view(), name = 'junta'),
    url(r'^contacto/', views.Contacto.as_view(), name = 'contacto'),
    url(r'^desarrollo/', views.Desarrollo.as_view(), name = 'desarrollo'),
]