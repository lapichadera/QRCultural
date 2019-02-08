from django.shortcuts import render, redirect
from .models import Sitio
from .forms import *
import qrcode

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
            img = qrcode.make("https://pypi.org/project/qrcode/")
            texto = sitio.nombre
            f = open("media/imagenQR/"+texto+".png", "wb")
            img.save(f)
            f.close()
            sitio.imgQR="/media/imagenQR/"+texto+".png"
            sitio.save()
            formulario.save_m2m()
            return redirect('/')
        else:
            formulario = sitio_form()
            print("no se está guardando")
    return render(request,"formulario.html",locals())


def vista_listar_sitios(request):
    lista = Sitio.objects.filter()
    return render(request,"listaSitios.html",locals())