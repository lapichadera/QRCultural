from django import forms
from .models import Sitio
class sitio_form(forms.ModelForm):
    class Meta:
        model = Sitio
        fields= '__all__'
        exclude= ["imgQR"]
