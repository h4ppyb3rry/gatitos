from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reservacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    numero_personas = models.PositiveIntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return str(self.nombre)