from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name = 'index'),
    url(r'^comunidad/', views.LaComunidad.as_view(), name = 'comunidad'),
]