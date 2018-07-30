from djongo import models
import csv

class Example(models.Model):

    nombre = models.CharField(max_length=255, blank=False)
    servicio = models.CharField(max_length=255, blank=False)
    ciudad = models.CharField(max_length=255, blank=False)
    total_factura = models.FloatField()
    fecha = models.DateTimeField()

    def getServicio(self):
        return self.servicio

    def getFecha(self):
        return self.fecha

    def __str__(self):
        return 'Nombre: %s\nServicio: %s\nCiudad: %s'%(self.nombre, self.servicio, self.ciudad)
