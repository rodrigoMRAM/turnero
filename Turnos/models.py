from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Turno(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.fecha} {self.hora_inicio} - {self.hora_fin}'
    

class Dia(models.Model):
    dia = models.CharField(max_length=10)
    horario1 = models.ForeignKey(Turno,on_delete=models.DO_NOTHING)

class TurnoEnProgreso(models.Model):
    turnoActual = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'   

    


# Create your models here.
