from django.shortcuts import render, redirect
from .models import Sitio
from .forms import *
import qrcode
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.

def vista_login(request):
    usuario=""
    clave=""
    if request.method== "POST":
        formulario = Login_form(request.POST)
        if formulario.is_valid():
            usuario= formulario.cleaned_data['usuario']
            clave= formulario.cleaned_data['clave']
            user= authenticate(username=usuario, password=clave)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("/adminis/opciones")
            else:
                msj = "usuario o clave incorrecto"

    formulario= Login_form()
    return render (request, "login.html", locals())

def vista_logout(request):
    logout(request)
    return redirect('/')

def vista_principal(request):
    return render(request,"index.html")

def vista_formulario(request):
    info_en=False
    formulario = sitio_form()
    inputTexts = ['nombre', 'anio', 'tipo1', 'apodo', 'horarios', 'horarios','arquitecto','patrono','ubicacion']

    if request.method== "POST":
        formulario = sitio_form(request.POST, request.FILES)
        if formulario.is_valid():
            info_en=True
            sitio=formulario.save(commit=False)
            id_proximo=Sitio.objects.count()+1
            img = qrcode.make("http://127.0.0.1:8000/sitio/"+str(id_proximo))
            texto = sitio.nombre
            f = open("media/imagenQR/"+texto+".png", "wb")
            img.save(f)
            f.close()
            sitio.imgQR="/media/imagenQR/"+texto+".png"
            sitio.save()
            formulario.save_m2m()
            return redirect('/adminis/opciones/lista')
        else:
            formulario = sitio_form()
            print("no se está guardando")
    return render(request,"formulario.html",locals())


def vista_listar_sitios(request):
    lista = Sitio.objects.filter()
    return render(request,"listaSitios.html",locals())

def vista_listar_sitios_crud(request):
    lista = Sitio.objects.filter()
    return render(request,"listaSitiosOp.html",locals())

def vista_detalle_sitio(request, id_s):
    sitio = Sitio.objects.get(id=id_s)
    return render(request,"detalle.html",locals())

def vista_opciones_admin(request):
    return render(request,"opciones.html",locals())

def vista_editar_sitio(request,id_s):
    sitio= Sitio.objects.get(id=id_s)
    if request.method=='POST':
        formulario= sitio_form(request.POST, request.FILES, instance=sitio)
        if formulario.is_valid:
            sitioM=formulario.save(commit=False)
            sitioM.save()
            return redirect('/adminis/opciones/lista')
        else:
            formulario= sitio_form(instance=sitio)

    formulario= sitio_form(instance=sitio)

    return render(request,'editarSitio.html',locals())

def vista_eliminar_sitio (request, id_s,user_id):
    user = User.objects.get(id=user_id)
    if user.is_active:
        sitioE= Sitio.objects.get(id=id_s)
        sitioE.delete()
    return redirect("/adminis/opciones/lista")