from django.urls import path, include
from .views import *
urlpatterns=[
    path('about/',vista_about),
    path('formulario/',vista_formulario)
]