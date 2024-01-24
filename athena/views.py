from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.urls import reverse
from .forms import formVulnerabilidad
from .models import Vulnerabilidad
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_vulnerabilidad(request):
    if request.method == 'POST':
        form = formVulnerabilidad()
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = formVulnerabilidad
    return render(request, 'formulario.html',{'form':form})