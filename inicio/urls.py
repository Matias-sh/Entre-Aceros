from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('steel_framing', views.steel_framing, name='steel_framing'),
    path('obras', views.obras, name="obras"),
    path('servicios', views.servicios, name="servicios"),
    path('proyecto/', views.proyecto, name="proyecto"),
    path('administracion/', views.administracion, name="administracion"),
    path('carpinteria/', views.carpinteria, name="carpinteria"),
    path('disenio/', views.disenio, name="disenio"),
    path('disenios_interiores/', views.disenios_interiores, name="disenios_interiores"),
    path('drywall/', views.drywall, name="drywall"),
    path('ejecucion_obras/', views.ejecucion_obras, name="ejecucion_obras"),
    path('estrucymon_galpones/', views.estrucymon_galpones, name="estrucymon_galpones"),
    path('estrucymon_techos/', views.estrucymon_techos, name="estrucymon_techos"),
    path('pintura/', views.pintura, name="pintura"),
    path('plomeria/', views.plomeria, name="plomeria"),
    path('remodelaciones/', views.remodelaciones, name="remodelaciones"),
    path('restauraciones/', views.restauraciones, name="restauraciones"),
    path('sist_electricos/', views.sist_electricos, name="sist_electricos"),
    path('steel_framing/', views.steel_framing, name="steel_framing")
]