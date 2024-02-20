from django import forms
from .models import Escaneo, Reporte, Vulnerabilidad, Target, Evidencia, Servicios

class formVulnerabilidad(forms.ModelForm):
    class Meta:
        model = Vulnerabilidad
        fields = ["nombre","cve","critico","descripcion","solucion"]
        CHOICES = ['leve','medio','HIGH']
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4 m-2 text-black w-80'}),
            'critico': forms.Select(attrs={'class': 'sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4 m-2 text-black'}),
            'cve': forms.TextInput(attrs={'class': 'sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4 m-2 h-10 text-black'}),
            'solucion': forms.Textarea(attrs={'class': 'w-1/2 sm:w-full p-4 h-20 m-2 text-black'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-1/2 sm:w-full p-4 h-30 m-2 text-black'}),
        }

class formTarget(forms.ModelForm):
    class Meta:
        model = Target
        fields =["nombre","ip","descripcion"]
        widgets = {
            'nombre':forms.TextInput(attrs={'class': 'sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4 m-2 text-black w-80'}),
            'ip':forms.TextInput(attrs={'class': 'sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4 m-2 text-black w-80'}),
            'descripcion':forms.TextInput(attrs={'class': 'sm:w-1/2 md:w-1/3 lg:w-1/4 xl:w-1/5 p-4 m-2 text-black w-80'})
        }
class formReporte(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ["vulnerabilidad","target","observacion"]
        widgets = {
            'vulnerabilidad': forms.Select(attrs={'class': 'w-1/2 sm:w-full p-4 h-20 m-2 text-black'}),
            'target': forms.Select(attrs={'class': 'w-1/2 sm:w-full p-4 h-20 m-2 text-black'}),
            'observacion': forms.Textarea(attrs={'class': 'w-1/2 sm:w-full p-4 h-30 m-2 text-black'})
            }

class formEvidencia(forms.ModelForm):
    class Meta:
        model = Evidencia
        fields = ["etapa","target","evidencia","descripcion"]
        widgets = {
            'etapa': forms.Select(attrs={'class': 'w-1/2 sm:w-full p-4 h-20 m-2 text-black'}),
            'target': forms.Select(attrs={'class': 'w-1/2 sm:w-full p-4 h-20 m-2 text-black'}),
            'evidencia': forms.FileInput(attrs={'class': 'w-1/2 sm:w-full p-4 h-20 m-2 text-black'}),
            'descripcion': forms.TextInput(attrs={'class': 'w-1/2 sm:w-full p-4 h-30 m-2 text-black'})
            }
class FormServicios(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ["nombre","descripcion"]

class FormEscaneo(forms.ModelForm):
    class Meta:
        model = Escaneo
        