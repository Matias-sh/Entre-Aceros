from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('steel_framing', views.steel_framing, name='steel_framing'),
    path('obras', views.obras, name="obras"),
    path('servicios', views.servicios, name="servicios"),
    path('proyecto/#proyecto', views.proyecto, name="proyecto"),
    path('disenio/#disenio', views.proyecto, name="disenio"),
    path('administracion/#administracion', views.proyecto, name="administracion")
]