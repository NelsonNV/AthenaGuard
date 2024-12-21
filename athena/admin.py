from django.contrib import admin
from .models import Target, Vulnerabilidad, Reporte, Evidencia, Servicios, Escaneo


class TargetAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ip", "descripcion")


class VulnerabilidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cve", "descripcion", "critico", "solucion")


class ReporteAdmin(admin.ModelAdmin):
    list_display = ("vulnerabilidad", "target", "observacion")


class EvidenciaAdmin(admin.ModelAdmin):
    list_display = ("etapa", "target", "descripcion")


class ServiciosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")


class EscaneoAdmin(admin.ModelAdmin):
    list_display = ("target", "servicio", "puerto")
    list_filter = ("servicio",)


admin.site.register(Target, TargetAdmin)
admin.site.register(Vulnerabilidad, VulnerabilidadAdmin)
admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Evidencia, EvidenciaAdmin)
admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Escaneo, EscaneoAdmin)
