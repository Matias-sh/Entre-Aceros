from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('steel_framing', views.steel_framing, name='steel_framing'),
    path('obras', views.obras, name="obras"),
    ## SERVICIOS
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
    path('steel_framing/', views.steel_framing, name="steel_framing"),
    ## OBRAS_DETALLES
    path('det_obras_calafate/', views.det_obras_calafate, name="det_obras_calafate"),
    path('det_obras_canton/', views.det_obras_canton, name="det_obras_canton"),
    path('det_obras_chalten/', views.det_obras_chalten, name="det_obras_chalten"),
    path('det_obras_eolicos/', views.det_obras_eolicos, name="det_obras_eolicos"),
    path('det_obras_fermar/', views.det_obras_fermar, name="det_obras_fermar"),
    path('det_obras_gral_rodriguez/', views.det_obras_gral_rodriguez, name="det_obras_gral_rodriguez"),
    path('det_obras_nuniez/', views.det_obras_nuniez, name="det_obras_nuniez"),
    path('det_obras_rio_gallegos/', views.det_obras_rio_gallegos, name="det_obras_rio_gallegos"),
    path('det_obras_sanmar/', views.det_obras_sanmar, name="det_obras_sanmar"),
    ## EMAIL
    path('envio', views.contacto, name="contacto")
]