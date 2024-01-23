from django import forms
from .models import Vulnerabilidad

class formVulnerabilidad(forms.ModelForm):
    class Meta:
        model = Vulnerabilidad
        fields = ["cve","descripcion","critico","solucion"]
        CHOICES = ['leve','medio','HIGH']
        widgets = { 
            'critico': forms.TextInput(attrs={'class': 'm-2 text-black'}),
            'cve': forms.TextInput(attrs={'class': 'm-2 text-black'}),
            'solucion': forms.Textarea(attrs={'class': 'm-2 text-black'}),
            'descripcion': forms.Textarea(attrs={'class': 'm-2 text-black'}),

        }