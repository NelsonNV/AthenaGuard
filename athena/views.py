from django.http import HttpResponseNotAllowed, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.urls import reverse
from .forms import FormEscaneo, FormServicios, formEvidencia, formVulnerabilidad, formTarget, formReporte
from .models import Escaneo, Evidencia, Reporte, Servicios, Target, Vulnerabilidad
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_vulnerabilidad(request):
    if request.method == 'POST':
        form = formVulnerabilidad(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = formVulnerabilidad
    return render(request, 'formulario.html',{'form':form})

def list_vulnerabilidad(request):
    vuln = list(Vulnerabilidad.objects.values())
    headers = [field.verbose_name for field in Vulnerabilidad._meta.fields]
    return render(request, 'listVuln.html', {'values': vuln,'headers':headers})

def edit_vulnerabilidad(request, id):
    obj = get_object_or_404(Vulnerabilidad, id=id)
    if request.method == "POST":
        form = formVulnerabilidad(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = formVulnerabilidad(instance=obj)

    return render(request, 'formulario.html', {'form': form})

def delete_vulnerabilidad(request, id):
    obj = get_object_or_404(Vulnerabilidad, id=id)
    try:
        obj.delete()
        messages.success(request, 'La vulnerabilidad ha sido eliminada con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar la vulnerabilidad: {str(e)}')
    return redirect('listVuln')

def add_target(request):
    if request.method == 'POST':
        form = formTarget(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = formTarget
    return render(request, 'formulario.html',{'form':form})

def list_target(request):
    targ = list(Target.objects.values())
    headers = [field.verbose_name for field in Target._meta.fields]
    return render(request, 'listTarget.html', {'values': targ,'headers':headers})

def edit_target(request, id):
    obj = get_object_or_404(Target, id=id)
    if request.method == "POST":
        form = formTarget(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = formTarget(instance=obj)

    return render(request, 'formulario.html', {'form': form})

def delete_target(request, id):
    obj = get_object_or_404(Target, id=id)
    try:
        obj.delete()
        messages.success(request, 'La vulnerabilidad ha sido eliminada con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar la vulnerabilidad: {str(e)}')
    return redirect('listVuln')

def report_target(request, target):
    infoTarget = get_object_or_404(Target, id=target)
    infoVuln = Reporte.objects.filter(target=target).select_related('vulnerabilidad')
    if request.method == 'POST':
        form = formReporte(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formReporte(initial={'target': infoTarget.id})
    return render(request,'reportTarget.html',{'infoTarget':infoTarget,'infoVuln':infoVuln,'form':form})
def edit_reporte(request, id_report):
    obj = get_object_or_404(Reporte, id=id_report)
    if request.method == "POST":
        form = formReporte(request.POST,instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = formReporte(instance=obj)
    return render(request,'formulario.html', {'form': form})

def delete_reporte(request,id_target , id_report):
    reporte = get_object_or_404(Reporte, id=id_report)
    try:
        reporte.delete()
        messages.success(request, 'El reporte ha sido eliminado con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar el reporte: {str(e)}')
    return redirect('viewReport', target=id_target)

def add_evidencia(request, id_report):
    reporte = get_object_or_404(Reporte, pk=id_report)

    if request.method == 'POST':        
        form = formEvidencia(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('viewReport', target=reporte.target.id)
    else:
        form = formEvidencia()
        form.initial['reporte'] = id_report
    return render(request, 'formulario.html',{'form':form})
def edit_evidencia(request, id_evidencia):
    evidencia = get_object_or_404(Evidencia, pk=id_evidencia)
    reporte_id = evidencia.reporte.id

    if request.method == 'POST':
        form = formEvidencia(request.POST, request.FILES, instance=evidencia)
        if form.is_valid():
            form.save()
            return redirect('viewReport', target=reporte_id)
    else:
        form = formEvidencia(instance=evidencia)

    return render(request, 'formulario.html', {'form': form, 'id_report': reporte_id})

def delete_evidencia(request, id_target, id_evidencia):
    evidencia = get_object_or_404(Evidencia, pk=id_evidencia)
    try:
        evidencia.delete()
        messages.success(request, 'La evidencia ha sido eliminada con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar la evidencia: {str(e)}')
    return redirect('viewReport', id_target=id_target)

def create_servicio(request):
    if request.method == 'POST':
        form = FormServicios(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listServ')
    else:
        form = FormServicios()
    return render(request, 'formulario.html', {'form': form})

def list_servicio(request):
    servicio = Servicios.objects.values()
    return render(request, 'servicios.html', {'servicio': servicio})

def update_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicios, id=servicio_id)
    if request.method == 'POST':
        form = FormServicios(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('listServ')
    else:
        form = FormServicios(instance=servicio)
    return render(request, 'formulario.html', {'form': form})

def delete_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicios, pk=servicio_id)
    try:
        servicio.delete()
        messages.success(request, 'El servicio ha sido eliminado con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar el servicio: {str(e)}')
    return redirect('listServ')
def create_escaneo(request):
    if request.method == 'POST':
        form = FormEscaneo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_escaneos')
    else:
        form = FormEscaneo()
    return render(request, 'formulario.html', {'form': form})

def read_escaneo(request, escaneo_id):
    escaneo = get_object_or_404(Escaneo, pk=escaneo_id)
    return render(request, 'detalle_escaneo.html', {'escaneo': escaneo})

def update_escaneo(request, escaneo_id):
    escaneo = get_object_or_404(Escaneo, pk=escaneo_id)
    if request.method == 'POST':
        form = FormEscaneo(request.POST, instance=escaneo)
        if form.is_valid():
            form.save()
            return redirect('detalle_escaneo', escaneo_id=escaneo_id)
    else:
        form = FormEscaneo(instance=escaneo)
    return render(request, 'editar_escaneo.html', {'form': form})

def delete_escaneo(request, id_target, id_escaneo):
    escaneo = get_object_or_404(Escaneo, pk=id_escaneo)
    try:
        escaneo.delete()
        messages.success(request, 'El escaneo ha sido eliminado con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar el escaneo: {str(e)}')
    return redirect('viewTarget', target=id_target)