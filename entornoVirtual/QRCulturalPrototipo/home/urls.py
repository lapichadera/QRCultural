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
    path('adminis/opciones/lista',vista_listar_sitios_crud,name='lista_sitios'),
    path('sitio/<int:id_s>/', vista_detalle_sitio,name='detalle_sitio'),
    path('adminis/opciones/agregarSitios',vista_formulario, name='formulario_sitios'),
    path('adminis/opciones/editarSitio/<int:id_s>/',vista_editar_sitio,name='editar_sitio'),
    path('adminis/opciones/eliminarSitio/<int:id_s>/<int:user_id>/',vista_eliminar_sitio,name='eliminar_sitio'),

]