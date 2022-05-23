from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

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

## VISTAS DET_OBRAS

def det_obras_calafate(request):
    return render(request, 'inicio/obras_detalles/calafate/obras_detalles.html')

def det_obras_canton(request):
    return render(request, 'inicio/obras_detalles/canton/obras_detalles.html')

def det_obras_chalten(request):
    return render(request, 'inicio/obras_detalles/el_chalten/obras_detalles.html')

def det_obras_eolicos(request):
    return render(request, 'inicio/obras_detalles/eolicos/obras_detalles.html')

def det_obras_fermar(request):
    return render(request, 'inicio/obras_detalles/fermar/obras_detalles.html')

def det_obras_gral_rodriguez(request):
    return render(request, 'inicio/obras_detalles/gral_rodriguez/obras_detalles.html')

def det_obras_nuniez(request):
    return render(request, 'inicio/obras_detalles/nuniez/obras_detalles.html')

def det_obras_rio_gallegos(request):
    return render(request, 'inicio/obras_detalles/rio_gallegos/obras_detalles.html')

def det_obras_sanmar(request):
    return render(request, 'inicio/obras_detalles/sanmar/obras_detalles.html')

## VISTAS PARA EL EMAIL

def contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('inicio/email_template.html', {
            'name': name,
            'subject': subject,
            'email': email,
            'message': message
        })

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,['devmatiasbritez@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo')
        return redirect('inicio')
