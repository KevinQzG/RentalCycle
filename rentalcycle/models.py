from django.db import models

# Create your models here.
class Campus(models.Model):
    id_campus = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    nombre_campus = models.CharField(max_length=20, verbose_name= 'Campus')     
    direccion_campus = models.CharField(max_length=15, verbose_name= 'Dirección')  
    
    def __str__(self):
        return self.nombre_campus

class Estudiante(models.Model):
    id_estudiante = models.CharField(primary_key=True, max_length=10, verbose_name= 'ID')
    primer_nombre_estudiante = models.CharField(max_length=20, verbose_name= 'Primer Nombre')
    primer_apellido_estudiante = models.CharField(max_length=20, verbose_name= 'Primer Apellido')
    carrera_estudiante = models.CharField(max_length=25, verbose_name= 'Carrera')    
    id_campus = models.ForeignKey(Campus, on_delete=models.CASCADE, db_column='id_campus', verbose_name= 'Campus')

    def __str__(self):
        return 'ID: ' + self.id_estudiante + ', Estudiante: ' + self.primer_nombre_estudiante + ' ' + self.primer_apellido_estudiante


class Alquiler(models.Model):
    codigo_alquiler = models.AutoField(primary_key=True, verbose_name= 'Código')    
    id_estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, db_column='id_estudiante', verbose_name= 'Estudiante')
    id_bicicleta = models.ForeignKey('Bicicleta', on_delete=models.CASCADE, db_column='id_bicicleta', verbose_name= 'Bicicleta')
    fecha_alquiler = models.DateTimeField(verbose_name= 'Fecha de Alquiler')
    fecha_prevista = models.DateField(blank=True, null=True, verbose_name= 'Fecha Prevista')
    fecha_devolucion = models.DateField(blank=True, null=True, verbose_name= 'Fecha de Devolución')
    dias_retraso = models.IntegerField(blank=True, null=True, verbose_name= 'Días de Retraso')

    def __str__(self):
        return 'Alquiler: ' + str(self.codigo_alquiler) + ', Estudiante: ' + self.id_estudiante.primer_nombre_estudiante + ' ' + self.id_estudiante.primer_apellido_estudiante + ', Fecha: ' + str(self.fecha_alquiler)[:10] 

    class Meta:
        unique_together = (('codigo_alquiler', 'id_estudiante', 'id_bicicleta', 'fecha_alquiler'))

class Bicicleta(models.Model):
    id_bicicleta = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    modelo_bicicleta = models.CharField(max_length=15, verbose_name='Modelo')  
    marca_bicicleta = models.CharField(max_length=15, verbose_name='Marca')   
    estado_bicicleta = models.CharField(max_length=20, verbose_name='Estado')
    precio_alquiler_bicicleta= models.IntegerField(verbose_name='Precio de Alquiler')  

    def __str__(self):
        return 'Bicicleta: ' + self.id_bicicleta + ', Modelo: ' + self.modelo_bicicleta + ', Marca: ' + self.marca_bicicleta

class CampusPromocion(models.Model):
    id_campus = models.OneToOneField(Campus, on_delete=models.CASCADE, db_column='id_campus', primary_key=True, verbose_name='Campus')        
    codigo_promocion = models.ForeignKey('Promocion', on_delete=models.CASCADE, db_column='codigo_promocion', verbose_name='Promoción')
    inicio_promocion = models.DateField(verbose_name='Fecha de Inicio')
    fin_promocion = models.DateField(verbose_name='Fecha de Fin')
        
    class Meta:
        unique_together = (('id_campus', 'codigo_promocion', 'inicio_promocion'))

    def __str__(self):
        return 'Promoción: ' + self.codigo_promocion + ', Campus: ' + self.id_campus.nombre_campus	

class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    primer_nombre_empleado = models.CharField(max_length=20, verbose_name='Primer Nombre')
    primer_apellido_empleado = models.CharField(max_length=20, verbose_name='Primer Apellido')
    cargo_empleado = models.CharField(max_length=25, verbose_name='Cargo')    

    def __str__(self):
        return 'ID: ' + self.id_empleado + ', Empleado: ' + self.primer_nombre_empleado + ' ' + self.primer_apellido_empleado

class Mantenimiento(models.Model):
    codigo_mantenimiento = models.CharField(primary_key=True, max_length=10, verbose_name='Código')
    id_bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE, db_column='id_bicicleta', verbose_name='Bicicleta')
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='id_empleado', verbose_name='Empleado')
    fecha_mantenimiento = models.DateField(verbose_name='Fecha')
    descripcion_mantenimiento = models.CharField(max_length=25, verbose_name='Descripción')
    
    def __str__(self):
        return 'Mantenimiento: ' +self.codigo_mantenimiento

class Promocion(models.Model):
    codigo_promocion = models.CharField(primary_key=True, max_length=10, verbose_name='Código')
    descripcion_promocion = models.CharField(max_length=25, verbose_name='Descripción')
    id_encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE, db_column='id_encargado', verbose_name='Encargado')

    def __str__(self):
        return 'Promoción: ' + self.codigo_promocion
    
