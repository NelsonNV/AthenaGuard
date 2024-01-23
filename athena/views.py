from django.shortcuts import render,redirect
from .forms import formVulnerabilidad
from .models import Vulnerabilidad
# Create your views here.
def home(request):
    vuln = Vulnerabilidad.objects.values
    return render(request,'home.html',{'vuln':vuln})

def add_vulnerabilidad(request):
    if request.method == 'POST':
        form = formVulnerabilidad
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = formVulnerabilidad
    return render(request, 'formulario.html',{'form':form})