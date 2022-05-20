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

def proyecto(request):
    return render(request, 'inicio/servicios/proyecto.html')