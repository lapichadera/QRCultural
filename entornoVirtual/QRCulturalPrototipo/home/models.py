from django.db import models

# Create your models here.
class Sitio (models.Model):
    nombre = models.CharField(max_length = 100)
    resenia = models.TextField(max_length = 500)
    imagen = models.ImageField(upload_to='imagen', null=True,blank= True)
    imagenTSS = models.ImageField(upload_to='imagen360', null=True,blank= True)
    imagenTSS1 = models.ImageField(upload_to='imagen360', null=True,blank= True)
    video = models.FileField(upload_to='video', null=True,blank= True)
    anio = models.IntegerField()
    tipo1 = models.CharField(max_length = 100)
    apodo = models.CharField(max_length = 100)
    horarios = models.CharField(max_length = 100)
    datosInteres = models.TextField(max_length = 500)
    arquitecto = models.CharField(max_length = 100)
    importanciaCiudad = models.TextField(max_length = 500)
    imagenR = models.ImageField(upload_to='imagen', null=True,blank= True)
    patrono = models.CharField(max_length = 100)
    principalesCambios = models.TextField(max_length = 500)
    ubicacion = models.CharField(max_length = 100)
    imgQR = models.CharField(max_length=500)
    def __str__(self):
        return self.nombre
