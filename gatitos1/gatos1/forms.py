from django import forms
from .models import Reservacion

class ResForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['nombre', 'numero_personas', 'hora', 'fecha']
