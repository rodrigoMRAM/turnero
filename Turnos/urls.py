from django.urls import path
from django.contrib import admin
from Turnos import views


urlpatterns = [
        path('admin/', admin.site.urls),
        path('turnos', views.saludo, name="Inicio"),
        path('turnos/dia0/', views.day0, name="dia0"),
        path('dia1/', views.day1, name="dia1"),
        path('dia2/', views.day2, name="dia2"),
        path('dia3/', views.day3, name="dia3"),
        path('dia4/', views.day4, name="dia4"),
        path('dia5/', views.day5, name="dia5"),
        path('dia6/', views.day6, name="dia6"),
        path('dia7/', views.day7, name="dia7"),
        path('dia8/', views.day8, name="dia8"),
        path('dia9/', views.day9, name="dia9"),
        path('dia10/', views.day10, name="dia10"),
        path('dia11/', views.day11, name="dia11"),
        path('dia12/', views.day12, name="dia12"),
        path('dia13/', views.day13, name="dia13"),
        path('dia14/', views.day14, name="dia14"),
        path('dia15/', views.day15, name="dia15"),
        path('dia16/', views.day16, name="dia16"),
        path('dia17/', views.day17, name="dia17"),
        path('dia18/', views.day18, name="dia18"),
        path('dia19/', views.day19, name="dia19"),
        path('dia20/', views.day20, name="dia20"),
        path('dia21/', views.day21, name="dia21"),
        path('dia22/', views.day22, name="dia22"),
        path('dia23/', views.day23, name="dia23"),
        path('dia24/', views.day24, name="dia24"),
        path('dia25/', views.day25, name="dia25"),
        path('dia26/', views.day26, name="dia26"),
        path('dia27/', views.day27, name="dia27"),
        path('dia28/', views.day28, name="dia28"),
        path('dia29/', views.day29, name="dia29"),
        path(r'^borrar/(?P<pk>\d+)$', views.TurnopedidoDelete.as_view(), name='Borrar'),
        path('turnopedidolist/', views.Turnopedidolist.as_view(), name='List'),

        path('agregar/' ,views.addDays, name="addDays")

]