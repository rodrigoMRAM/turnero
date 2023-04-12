
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from Turnos.models import Turno
from Turnos.forms import AgregarDias, CustomAuthenticationForm
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from urllib import request
from django.views import generic
from Turnos.forms import ToDoForm

# def saludo(request):
#     midato = Turnopedido.objects.all()
#     return render(request,"Turnos/index.html", {"datos": midato})
# def addDays(request):
#     for a in range(1, 31):
#         nuevoDia = Turnopedido(dia= a,hora=10,hora1=11,hora2=12,hora3=13 ,hora4=14, clase= a)
#         nuevoDia.save()

def inicio(request):
    return render(request, 'Turnos/index.html')
class PanelLogin(LoginView):
    template_name = "Turnos/turnos_login.html"
    next_page = reverse_lazy("Listar")
    authentication_form = CustomAuthenticationForm

class PanelLogout(LogoutView):
    template_name = 'Turnos/turnos.html'
# def day0(request):
#     midato = Turnopedido.objects.all()
#     context0 = Turnopedido.objects.all()[0]
#     context1 = Turnopedido.objects.all()[1]
#     context2 = Turnopedido.objects.all()[2]
#     context3 = Turnopedido.objects.all()[3]
#     context4 = Turnopedido.objects.all()[4]
#     context5 = Turnopedido.objects.all()[5]
#     context6 = Turnopedido.objects.all()[6]
#     return render(request, "Turnos/dia0.html",{"datos": midato,"context0" : context0, 
#     "context1": context1,
#     "context2": context2,
#     "context3": context3,
#     "context4": context4,
#     "context5": context5,
#     "context6": context6})

# def day1(request):
#     context1 = Turnopedido.objects.all()[1]
#     return render(request, "Turnos/dia1.html", {"context1" : context1})

# def day2(request):
#     context2 = Turnopedido.objects.all()[2]
#     return render(request, "Turnos/dia2.html", {"context2" : context2})    


# def day3(request):
#     context3 = Turnopedido.objects.all()[3]
#     return render(request, "Turnos/dia3.html", {"context3" : context3})

# def day4(request):
#     context4 = Turnopedido.objects.all()[4]
#     return render(request, "Turnos/dia4.html", {"context4" : context4})

# def day5(request):
#     context5 = Turnopedido.objects.all()[5]
#     return render(request, "Turnos/dia5.html", {"context5" : context5})
# def day6(request):
#     context6 = Turnopedido.objects.all()[6]
#     return render(request, "Turnos/dia6.html", {"context6" : context6})

# def day7(request):
#     context7 = Turnopedido.objects.all()[7]
#     return render(request, "Turnos/dia7.html", {"context7" : context7})

# def day8(request):
#     context8 = Turnopedido.objects.all()[8]
#     return render(request, "Turnos/dia8.html", {"context8" : context8})
# def day9(request):
#     context9 = Turnopedido.objects.all()[9]
#     return render(request, "Turnos/dia9.html", {"context9" : context9})
# def day10(request):
#     context10 = Turnopedido.objects.all()[10]
#     return render(request, "Turnos/dia10.html", {"context10" : context10})
# def day11(request):
#     context11 = Turnopedido.objects.all()[11]
#     return render(request, "Turnos/dia11.html", {"context11" : context11})
# def day12(request):
#     context12 = Turnopedido.objects.all()[12]
#     return render(request, "Turnos/dia12.html", {"context12" : context12})
# def day13(request):
#     context13 = Turnopedido.objects.all()[13]
#     return render(request, "Turnos/dia13.html", {"context13" : context13})
# def day14(request):
#     context14 = Turnopedido.objects.all()[14]
#     return render(request, "Turnos/dia14.html", {"context14" : context14})
# def day15(request):
#     context15 = Turnopedido.objects.all()[15]
#     return render(request, "Turnos/dia15.html", {"context15" : context15})
# def day16(request):
#     context16 = Turnopedido.objects.all()[16]
#     return render(request, "Turnos/dia16.html", {"context16" : context16})
# def day17(request):
#     context17 = Turnopedido.objects.all()[17]
#     return render(request, "Turnos/dia17.html", {"context17" : context17})

# def day18(request):
#     context18 = Turnopedido.objects.all()[18]
#     return render(request, "Turnos/dia18.html", {"context18" : context18})
# def day19(request):
#     context19 = Turnopedido.objects.all()[19]
#     return render(request, "Turnos/dia19.html", {"context19" : context19})
# def day20(request):
#     context20 = Turnopedido.objects.all()[20]
#     return render(request, "Turnos/dia20.html", {"context20" : context20})
# def day21(request):
#     context21 = Turnopedido.objects.all()[21]
#     return render(request, "Turnos/dia21.html", {"context21" : context21})
# def day22(request):
#     context22 = Turnopedido.objects.all()[22]
#     return render(request, "Turnos/dia22.html", {"context22" : context22})
# def day23(request):
#     context23 = Turnopedido.objects.all()[23]
#     return render(request, "Turnos/dia23.html", {"context23" : context23})
# def day24(request):
#     context24 = Turnopedido.objects.all()[24]
#     return render(request, "Turnos/dia24.html", {"context24" : context24})
# def day25(request):
#     context25 = Turnopedido.objects.all()[25]
#     return render(request, "Turnos/dia25.html", {"context25" : context25})
# def day26(request):
#     context26 = Turnopedido.objects.all()[26]
#     return render(request, "Turnos/dia26.html", {"context26" : context26})

# def day25(request):
#     context25 = Turnopedido.objects.all()[25]
#     return render(request, "Turnos/dia25.html", {"context25" : context25})
# def day26(request):
#     context26 = Turnopedido.objects.all()[26]
#     return render(request, "Turnos/dia26.html", {"context26" : context26})
# def day27(request):
#     context27 = Turnopedido.objects.all()[27]
#     return render(request, "Turnos/dia27.html", {"context27" : context27})

    
# def day29(request):
#     context29 = Turnopedido.objects.all()[29]
#     return render(request, "Turnos/dia29.html", {"context29" : context29})
# def day28(request):
#     context28 = Turnopedido.objects.all()[28]
#     return render(request, "Turnos/dia28.html", {"context28" : context28})





# class TurnopedidoDelete(DeleteView):

#     model= Turnopedido
#     success_url= "/turnopedidolist/"

# class Turnopedidolist(ListView):

#     model = Turnopedido
#     Template_name = "Turnos/dias_list.html"


class CustomFormView(generic.FormView):
    template_name = "Turnos/custom-form.html"
    form_class = ToDoForm





def listar_turnos(request):
    turnos = Turno.objects.all().order_by('fecha', 'hora_inicio')
    return render(request, 'Turnos/turnos.html', {'turnos': turnos})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def asignar_turno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    if request.method == 'POST':
        if not turno.asignado_a:
            turno.asignado_a = request.user
            turno.activo = False
            turno.save()
            context={
                "texto" : "Turno {turno} asignado a {request.user.username}"
            }
            print(context['texto'])
            render(request,'Turnos/asignar_turno.html', context)
            # messages.success(request, f'Turno {turno} asignado a {request.user.username}')
        else:
            messages.warning(request, f'El turno {turno} ya está asignado a {turno.asignado_a.username}')
        return render(request, 'Turnos/turnos.html', {"mensaje": "Se realizo la reserva correctamente"})
    return render(request, 'Turnos/asignar_turno.html', {'turno': turno})


def eliminar_reserva(request, id):
    turno = get_object_or_404(Turno, pk= id)
    if request.method == 'POST':
        if turno.asignado_a:
            turno.asignado_a = None
            turno.activo = True
            turno.save()
            mensaje = "Se elimino correctamente"
            render(request,'Turnos/confirm_delete_reserve.html' )
        else:
            messages.warning(request, f'El turno {turno} ya está asignado ')
        return render(request, 'Turnos/turnos.html', {"mensaje": "Se eliminó la reserva correctamente"})
    return render(request, 'Turnos/confirm_delete_reserve.html', {'turno': turno})



def recolectando(request, id):
    horaInicio=  Turno.objects.filter(fecha__startswith=id)
    return render(request ,'Turnos/filtro.html' , {"horaInicio": horaInicio})
# , {"turno":turno}

def prueba(request):
    lista = ["09" , "10", "12", "14"]
    dias = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
    for l in dias:
        for x in range(4):
            h=  Turno(fecha=f"2023-04-{l}",hora_inicio=lista[x], hora_fin="20", asignado_a=None, activo=True)
            h.save()



