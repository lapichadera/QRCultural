from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns=[
    path('admin/',admin.site.urls ),
    path('',vista_principal, name='index'),
    path('formulario/',vista_formulario),
    path('sitios/',vista_listar_sitios, name='sitios'),
    path('sitio/<int:id_s>/', vista_detalle_sitio,name='detalle_sitio'),

]