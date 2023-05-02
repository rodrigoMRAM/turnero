from django.urls import path
from django.contrib import admin
from Turnos.views import * 


urlpatterns = [
         path('admin/', admin.site.urls),
        path('inicio/',CustomFormView.as_view(), name="Formulario"),
        # path('turnos/', saludo, name="Inicio"),
        # path('turnos/dia0/', day0, name="dia0"),
        # path('dia1/', day1, name="dia1"),
        # path('dia2/', day2, name="dia2"),
        # path('dia3/', day3, name="dia3"),
        # path('dia4/', day4, name="dia4"),
        # path('dia5/', day5, name="dia5"),
        # path('dia6/', day6, name="dia6"),
        # path('dia7/', day7, name="dia7"),
        # path('dia8/', day8, name="dia8"),
        # path('dia9/', day9, name="dia9"),
        # path('dia10/', day10, name="dia10"),
        # path('dia11/', day11, name="dia11"),
        # path('dia12/', day12, name="dia12"),
        # path('dia13/', day13, name="dia13"),
        # path('dia14/', day14, name="dia14"),
        # path('dia15/', day15, name="dia15"),
        # path('dia16/', day16, name="dia16"),
        # path('dia17/', day17, name="dia17"),
        # path('dia18/', day18, name="dia18"),
        # path('dia19/', day19, name="dia19"),
        # path('dia20/', day20, name="dia20"),
        # path('dia21/', day21, name="dia21"),
        # path('dia22/', day22, name="dia22"),
        # path('dia23/', day23, name="dia23"),
        # path('dia24/', day24, name="dia24"),
        # path('dia25/', day25, name="dia25"),
        # path('dia26/', day26, name="dia26"),
        # path('dia27/', day27, name="dia27"),
        # path('dia28/', day28, name="dia28"),
        # path('dia29/', day29, name="dia29"),
        # path(r'^borrar/(?P<pk>\d+)$', TurnopedidoDelete.as_view(), name='Borrar'),
        # path('turnopedidolist/', Turnopedidolist.as_view(), name='List'),

        # path('agregar/' ,addDays, name="addDays")
        path("inicio/", inicio, name="inicio"),
        path("", listar_turnos, name="Listar"),
        path('asignar/<id>/', asignar_turno, name="Asignar"),
        path('eliminar/<id>/', eliminar_reserva, name="Eliminar"),
        path('recolectando/<id>', recolectando, name="recolecta"),
        path('prueba/', prueba, name="prueba"),
        path("login/", PanelLogin.as_view(), name="panel-login"),
        path("logout/", PanelLogout.as_view(), name="panel-logout"),
        path("misTurnos/" , misTurnos, name="misTurnos")
]