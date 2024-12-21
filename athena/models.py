from django.db import models


class Vulnerabilidad(models.Model):
    CRITICO_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    nombre = models.CharField(max_length=150)
    cve = models.CharField(max_length=50)
    descripcion = models.TextField()
    critico = models.CharField(max_length=10, choices=CRITICO_CHOICES)

    solucion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"


class Target(models.Model):
    nombre = models.CharField(max_length=100)
    ip = models.CharField(max_length=12)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"


class Reporte(models.Model):
    vulnerabilidad = models.ForeignKey(Vulnerabilidad, on_delete=models.CASCADE)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    observacion = models.TextField()

    def __str__(self):
        return f"{self.vulnerabilidad.nombre}"


class Evidencia(models.Model):
    ETAPAS_REPORT = [
        ("reconocimiento", "Reconocimiento"),
        ("escaneo", "Escaneo"),
        ("exploit", "Exploit"),
    ]
    etapa = models.CharField(max_length=15, choices=ETAPAS_REPORT)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    evidencia = models.ImageField(upload_to="evidencias/")
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.etapa}, {self.target.nombre}"


class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"


class Escaneo(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    servicio = models.ForeignKey(
        Servicios, on_delete=models.CASCADE, null=True, blank=True
    )
    puerto = models.IntegerField()

    def __str__(self):
        return f"{self.target.nombre}"
