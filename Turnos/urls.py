from django.urls import path
from django.contrib import admin
from Turnos.views import * 


urlpatterns = [
        path("inicio/", inicio, name="inicio"),
        path("listar/", listar_turnos, name="Listar"),
        path('asignar/<id>/', asignar_turno, name="Asignar"),
        path('eliminar/<id>/', eliminar_reserva, name="Eliminar"),
        path('recolectando/<id>', recolectando, name="recolecta"),
        path('prueba/', prueba, name="prueba"),
        path("misTurnos/" , misTurnos, name="misTurnos"),
        # LOGIN Y REGISTRO
        path("", PanelLogin.as_view(), name="panel-login"),
        path("logout/", PanelLogout.as_view(), name="panel-logout"),
        path("register/", register, name="register"),
]