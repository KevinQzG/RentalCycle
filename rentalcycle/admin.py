from django.contrib import admin, messages
from .utils import cantidad_alquileres, actualizar_dias_retraso
from .models import *

#Clases para registrar los modelos en el panel de administracion
admin.site.register(CampusPromocion)
admin.site.register(Mantenimiento)
admin.site.register(Promocion)

#Configuracion del panel de administracion
admin.site.site_header = 'Rentalcycle'
admin.site.index_title = 'Panel de administrador'
admin.site.site_title = 'Rentalcycle'
admin.site.icon= 'static/rentalcycle/img/logo.png'

#Accion en estudiante para llamar a la funcion para retornar la cantidad de alquileres
class EstudianteAdmin(admin.ModelAdmin):
    search_fields = ('id_estudiante', 'primer_nombre_estudiante', 'primer_apellido_estudiante')
    def cantidad_alquileres(modeladmin, request, queryset):
        for estudiante in queryset:
            resultado = cantidad_alquileres(estudiante.id_estudiante)
            if resultado is None: messages.success(request, 'El estudiante no ha realizado alquileres')
            else: messages.success(request, resultado)
    actions = [cantidad_alquileres]

admin.site.register(Estudiante, EstudianteAdmin)

#Accion en alquiler para llamar al procedimiento almacenado para actualizar los dias de retraso
class AlquilerAdmin(admin.ModelAdmin):
    search_fields = ('codigo_alquiler', 'id_estudiante__primer_nombre_estudiante', 'fecha_alquiler')
    def ejecutar_accion(self, request, queryset):
        actualizar_dias_retraso()
        self.message_user(request, "Se han actualizado los días de retraso de los alquileres")

    ejecutar_accion.short_description = "Actualizar días de retraso"

    actions = [ejecutar_accion]

admin.site.register(Alquiler, AlquilerAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    search_fields = ('id_empleado', 'primer_nombre_empleado', 'primer_apellido_empleado')

admin.site.register(Empleado, EmpleadoAdmin)

class BicicletaAdmin(admin.ModelAdmin):
    search_fields = ('id_bicicleta', 'modelo_bicicleta', 'marca_bicicleta', 'estado_bicicleta')

admin.site.register(Bicicleta, BicicletaAdmin)


class CampusAdmin(admin.ModelAdmin):
    search_fields = ('id_campus', 'nombre_campus')

admin.site.register(Campus, CampusAdmin)
