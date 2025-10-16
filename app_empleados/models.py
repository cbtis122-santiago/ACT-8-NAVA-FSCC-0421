from django.db import models

class Empleado(models.Model):

    id_empleado = models.CharField(max_length=10, unique=True)
    id_sucursal = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'Empleado: {self.nombre} {self.apellido} - Cargo: {self.cargo}'