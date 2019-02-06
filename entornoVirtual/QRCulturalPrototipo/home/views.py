from django.shortcuts import render
from .forms import *

# Create your views here.

def vista_about(request):
    return render(request,"about.html")

def vista_formulario(request):
    info_en= False
    nombre = ""
    resenia = ""
    imagen = ""
    imagenTSS = ""
    imagenTSS1 = ""
    video = ""
    anio = ""
    tipo = ""
    apodo = ""
    horarios = ""
    datosInteres = ""
    arquitecto = ""
    importanciaCiudad = ""
    imagenR = ""
    patrono = ""
    principalesCambios = ""
    ubicacion = ""
    formulario = sitio_form()
    if request.method== "POST":
        formulario = sitio_form(request.POST)
        if formulario.is_valid():
            info_en=True
            nombre = formulario.cleaned_data['nombre']
            resenia = formulario.cleaned_data['resenia']
            imagen = formulario.cleaned_data['imagen']
            imagenTSS = formulario.cleaned_data['imagen']
            imagenTSS1 = formulario.cleaned_data['imagen']
            video = formulario.cleaned_data['video']
            anio = formulario.cleaned_data['anio']
            tipo = formulario.cleaned_data['tipo']
            apodo = formulario.cleaned_data['apodo']
            horarios = formulario.cleaned_data['horarios']
            datosInteres = formulario.cleaned_data['datosInteres']
            arquitecto = formulario.cleaned_data['arquitecto']
            importanciaCiudad = formulario.cleaned_data['importanciaCiudad']
            imagenR = formulario.cleaned_data['imagenR']
            patrono = formulario.cleaned_data['patrono']
            principalesCambios = formulario.cleaned_data['principalesCambios']
            ubicacion = formulario.cleaned_data['ubicacion']

        else:
            formulario = sitio_form()
    return render(request,"formulario.html",locals())
