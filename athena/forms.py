from django import forms
from .models import Escaneo, Reporte, Vulnerabilidad, Target, Evidencia, Servicios


class CustomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not field.label:
                field.label = field_name.replace("_", " ").capitalize()
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' block font-medium text-gray-600 mb-2'

class formVulnerabilidad(CustomForm):
    class Meta:
        model = Vulnerabilidad
        fields = ["nombre", "cve", "critico", "descripcion", "solucion"]
        labels = {
            'nombre': 'Nombre de la Vulnerabilidad',
            'cve': 'Código CVE',
            'critico': 'Nivel Crítico',
            'descripcion': 'Descripción Detallada',
            'solucion': 'Solución Propuesta',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'critico': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'cve': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'solucion': forms.Textarea(attrs={'class': 'w-full max-w-lg p-2 m-2 border rounded text-gray-800'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full max-w-lg p-2 m-2 border rounded text-gray-800'}),
        }

class formTarget(CustomForm):

    class Meta:
        model = Target
        fields =["nombre","ip","descripcion"]
        labels = {
            'nombre': 'Nombre del Target',
            'ip': 'IP del Target',
            'descripcion': 'Descripción Detallada',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'ip': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'descripcion': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
        }

class formReporte(CustomForm):
    class Meta:
        model = Reporte
        fields = ["vulnerabilidad","target","observacion"]
        labels = {
            'vulnerabilidad': 'Vulnerabilidad',
            'target': 'Target',
            'observacion': 'Observaciones',
        }
        widgets = {
            'vulnerabilidad': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'target': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'observacion': forms.Textarea(attrs={'class': 'w-full max-w-lg p-2 m-2 border rounded text-gray-800'}),
        }

class formEvidencia(CustomForm):
    class Meta:
        model = Evidencia
        fields = ["etapa", "target", "evidencia", "descripcion"]
        widgets = {
            'etapa': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'target': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'evidencia': forms.FileInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'descripcion': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
        }

class FormServicios(CustomForm):
    class Meta:
        model = Servicios
        fields = ["nombre", "descripcion"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'descripcion': forms.TextInput(attrs={'class': 'w-full max-w-lg p-2 m-2 border rounded text-gray-800'}),
        }

class FormEscaneo(CustomForm):
    class Meta:
        model = Escaneo
        fields = ['target', 'servicio', 'puerto']
        widgets = {
            'target': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'servicio': forms.Select(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
            'puerto': forms.NumberInput(attrs={'class': 'w-full max-w-md p-2 m-2 border rounded text-gray-800'}),
        }
