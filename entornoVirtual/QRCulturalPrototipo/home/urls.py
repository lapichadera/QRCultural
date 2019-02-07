from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',vista_principal),
    path('formulario/',vista_formulario),
    path('lista/',vista_listar_sitios),
]