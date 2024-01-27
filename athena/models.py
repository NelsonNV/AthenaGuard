from django.db import models

class Vulnerabilidad(models.Model):
    CRITICO_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    nombre = models.CharField(max_length=150)
    cve = models.CharField(max_length=50)
    descripcion = models.TextField()
    critico = models.CharField(max_length=10, choices=CRITICO_CHOICES)

    solucion = models.TextField()
    def __str__(self):
        return self.nombre
class Target(models.Model):
    nombre = models.CharField(max_length=100)
    ip = models.CharField(max_length=12)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre

class Reporte(models.Model):
    vulnerabilidad = models.ForeignKey(Vulnerabilidad,on_delete=models.CASCADE)
    target = models.ForeignKey(Target,on_delete=models.CASCADE)
    observacion = models.TextField()
class Evidencia(models.Model):
    reporte = models.ForeignKey(Reporte,on_delete=models.CASCADE)
    evidencia = models.ImageField(upload_to='evidencias/')