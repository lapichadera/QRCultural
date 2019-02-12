from django import forms
from .models import Sitio
class sitio_form(forms.ModelForm):
    class Meta:
        model = Sitio
        fields= '__all__'
        labels={
            'resenia':("Reseña"),
            'imagenTSS':("Imagen 360 interior"),
            'imagenTSS1':("Imagen 360 exterior"),
        	'anio':('Año'),
        	'tipo1':('Tipo'),
        	'ubicacion':('Ubicación'),
            'principalesCambios':('Principales cambios'),
            'importanciaCiudad':('Importacia para la ciudad'),
            'datosInteres':('Datos de interés'),

        }
        exclude= ["imgQR"]
        widgets={
            'anio': forms.TextInput(attrs={'class':'datepicker'}),
            
        }

class Login_form(forms.Form):
	usuario= forms.CharField(widget=forms.TextInput())
	clave= forms.CharField(widget=forms.PasswordInput(render_value=True))
