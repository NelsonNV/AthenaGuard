from django.db import models

class Vugnerabilidad(models.Model):
    cve = models.CharField(max_length=50)
    descripcion = models.TextField()
    critico = models.CharField(max_length=50)
    solucion = models.TextField()

class Target(models.Model):
    nombre = models.CharField(max_length=100)
    ip = models.CharField(max_length=12)
    descripcion = models.TextField()

class Reporte(models.Model):
    vugnerabilidad = models.ForeignKey(Vugnerabilidad,on_delete=models.CASCADE)
    target = models.ForeignKey(Target,on_delete=models.CASCADE)