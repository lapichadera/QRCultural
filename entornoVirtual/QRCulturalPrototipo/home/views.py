from django.shortcuts import render, redirect
from .models import Sitio
from .forms import *

# Create your views here.

def vista_principal(request):
    return render(request,"index.html")

def vista_formulario(request):
    info_en=False
    formulario = sitio_form()

    if request.method== "POST":
        formulario = sitio_form(request.POST, request.FILES)
        if formulario.is_valid():
            info_en=True
            sitio=formulario.save(commit=False)
            sitio.save()
            formulario.save_m2m()
            return redirect('/')
        else:
            formulario = sitio_form()
    return render(request,"formulario.html",locals())


def vista_listar_sitios(request):
    lista = Sitio.objects.filter()
    return render(request,"listaSitios.html",locals())