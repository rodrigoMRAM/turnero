from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("myapp:model-form", kwargs={"pk": self.pk})

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
