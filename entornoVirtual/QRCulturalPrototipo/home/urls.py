from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns=[
    path('admin/',admin.site.urls ),
    path('',vista_principal, name='index'),
    path('sitios/',vista_listar_sitios, name='sitios'),
    path('sitio/<int:id_s>/', vista_detalle_sitio,name='detalle_sitio'),
    path('login/', vista_login,name='login'),
    path('logout',vista_logout,name='logout'),
    path('adminis/opciones',vista_opciones_admin,name='opciones'),
    path('adminis/opciones/sitios',vista_formulario, name='formulario_sitios'),

]