from django.urls import path
from django.contrib import admin
from Turnos.views import * 


urlpatterns = [
         path('admin/', admin.site.urls),
        path('inicio/',CustomFormView.as_view(), name="Formulario"),
        # path("inicio/", inicio, name="inicio"),
        path("", listar_turnos, name="Listar"),
        path('asignar/<id>/', asignar_turno, name="Asignar"),
        path('eliminar/<id>/', eliminar_reserva, name="Eliminar"),
        path('recolectando/<id>', recolectando, name="recolecta"),
        path('prueba/', prueba, name="prueba"),
        path("login/", PanelLogin.as_view(), name="panel-login"),
        path("logout/", PanelLogout.as_view(), name="panel-logout"),
        path("misTurnos/" , misTurnos, name="misTurnos"),
        path("/register", register, name="register")
]