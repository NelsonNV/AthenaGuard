from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.urls import reverse
from .forms import formEvidencia, formVulnerabilidad, formTarget, formReporte
from .models import Reporte, Target, Vulnerabilidad
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
    obj = get_object_or_404(formTarget, id=id)
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
    print(f"id_report: {id_report}, id_target: {id_target}")
    reporte = get_object_or_404(Reporte, id=id_report)
    print(f"reporte: {reporte}")
    try:
        reporte.delete()
        messages.success(request, 'El reporte ha sido eliminado con éxito.')
    except Exception as e:
        messages.error(request, f'Error al intentar eliminar el reporte: {str(e)}')
    print("redirecting to")
    return redirect('viewReport', target=id_target)

