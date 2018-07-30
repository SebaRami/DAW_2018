from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
		return self.nombre

class Servicio(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nombre_servicio = models.CharField(max_length=200)

	def __str__(self):
		return self.usuario.nombre + " - " + self.nombre_servicio
