from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# class Event(models.Model):
#     name = models.CharField(max_length=200)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     start_datetime = models.DateTimeField()
#     end_datetime = models.DateTimeField()

#     def __str__(self) -> str:
#         return self.name

#     def get_absolute_url(self) -> str:
#         return reverse("myapp:model-form", kwargs={"pk": self.pk})


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
    horario1 = models.ForeignKey(Turno,on_delete=models.DO_NOTHING)
    


# Create your models here.
