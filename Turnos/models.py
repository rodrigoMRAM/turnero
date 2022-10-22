from django.db import models
from django.contrib.auth.models import User

class Turnopedido(models.Model):
    dia = models.IntegerField()
    hora = models.IntegerField()
    hora1 = models.IntegerField()
    hora2 = models.IntegerField()
    hora3 = models.IntegerField()
    hora4 = models.IntegerField()
    clase = models.IntegerField()
    def __str__(self):
    
     return f"dia: {self.dia} - Hora: {self.hora} - Hora: {self.hora1} - Hora: {self.hora2}- Hora: {self.hora3} - Hora: {self.hora4} -  Clase: {self.clase}"

# Create your models here.
