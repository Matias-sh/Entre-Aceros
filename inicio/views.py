from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio/index.html')


def steel_framing(request):
    return render(request, 'inicio/steel_framing.html')

def obras(request):
    return render(request, 'inicio/obras.html')

def servicios(request):
    return render(request, 'inicio/servicios.html')

## VISTAS SERVICIOS

def proyecto(request):
    return render(request, 'inicio/servicios/proyecto/servicio.html')

def administracion(request):
    return render(request, 'inicio/servicios/administracion/servicio.html')

def carpinteria(request):
    return render(request, 'inicio/servicios/carpinteria/servicio.html')

def disenio(request):
    return render(request, 'inicio/servicios/disenio/servicio.html')

def disenios_interiores(request):
    return render(request, 'inicio/servicios/disenios_interiores/servicio.html')

def drywall(request):
    return render(request, 'inicio/servicios/drywall/servicio.html')

def ejecucion_obras(request):
    return render(request, 'inicio/servicios/ejecucion_obras/servicio.html')

def estrucymon_galpones(request):
    return render(request, 'inicio/servicios/estrucymon_galpones/servicio.html')

def estrucymon_techos(request):
    return render(request, 'inicio/servicios/estrucymon_techos/servicio.html')

def pintura(request):
    return render(request, 'inicio/servicios/pintura/servicio.html')

def plomeria(request):
    return render(request, 'inicio/servicios/plomeria/servicio.html')

def remodelaciones(request):
    return render(request, 'inicio/servicios/remodelaciones/servicio.html')

def restauraciones(request):
    return render(request, 'inicio/servicios/restauraciones/servicio.html')

def sist_electricos(request):
    return render(request, 'inicio/servicios/sist_electricos/servicio.html')

def steel_framing(request):
    return render(request, 'inicio/servicios/steel_framing/servicio.html')