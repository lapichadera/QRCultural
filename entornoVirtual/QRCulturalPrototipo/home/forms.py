from django import forms

class sitio_form(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    resenia = forms.CharField(widget=forms.Textarea)
    imagen = forms.CharField(widget=forms.TextInput)
    imagenTSS = forms.CharField(widget=forms.TextInput)
    imagenTSS1 = forms.CharField(widget=forms.TextInput)
    video = forms.CharField(widget=forms.TextInput)
    anio = forms.CharField(widget=forms.TextInput)
    tipo = forms.CharField(widget=forms.TextInput)
    apodo = forms.CharField(widget=forms.TextInput)
    horarios = forms.CharField(widget=forms.TextInput)
    datosInteres = forms.CharField(widget=forms.TextInput)
    arquitecto = forms.CharField(widget=forms.TextInput)
    importanciaCiudad = forms.CharField(widget=forms.TextInput)
    imagenR = forms.CharField(widget=forms.TextInput)
    patrono = forms.CharField(widget=forms.TextInput)
    principalesCambios = forms.CharField(widget=forms.TextInput)
    ubicacion = forms.CharField(widget=forms.TextInput)
    
