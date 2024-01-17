
from datetime import datetime ,timedelta
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from Turnos.models import Turno
from Turnos.forms import AgregarDias, CustomAuthenticationForm , UserRegisterForm
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic.edit import CreateView ,UpdateView
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
    miTurno = Turno.objects.filter(asignado_a=request.user)
    return render(request, 'Turnos/index.html', {"miTurno": miTurno})
class PanelLogin(LoginView):
    template_name = "Turnos/turnos_login.html"
    next_page = reverse_lazy("Listar")
    authentication_form = CustomAuthenticationForm

class PanelLogout(LogoutView):
    template_name = 'Turnos/turnos.html'




# class TurnopedidoDelete(DeleteView):

#     model= Turnopedido
#     success_url= "/turnopedidolist/"

# class Turnopedidolist(ListView):

#     model = Turnopedido
#     Template_name = "Turnos/dias_list.html"


class CustomFormView(generic.FormView):
    template_name = "Turnos/custom-form.html"
    form_class = ToDoForm




# PAGINA PRINCIPAL, CALENDARIO
def listar_turnos(request):
    turnos = Turno.objects.all().order_by('fecha', 'hora_inicio')
    miTurno = Turno.objects.filter(asignado_a=request.user)
    return render(request, 'Turnos/turnos.html', {'turnos': turnos, "miTurno": miTurno})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# FUNCION DE ASIGNAR UN TURNO
@login_required
def asignar_turno(request, id):
    turno = get_object_or_404(Turno, pk=id)
    #VERIFICANDO SI TIENE TURNOS ASIGNADOS
    for e in Turno.objects.all():
        if e.asignado_a == request.user:
            return render(request,'Turnos/imposible.html' )
        # ESTE CODIGO ASIGNA EL TURNO SI ES QUE NO POSEE UNO
        else:
            if request.method == 'POST':
                if not turno.asignado_a:
                    turno.asignado_a = request.user
                    turno.activo = False
                    turno.save()
                    context={
                        "texto" : f"Turno {turno} asignado a {request.user.username}"
                    }
                    render(request,'Turnos/asignar_turno.html', context)
                else:
                    messages.warning(request, f'El turno {turno} ya está asignado a {turno.asignado_a.username}')
                    context={
                        "texto" : "Turno {turno} asignado a {request.user.username}"
                    }
                return render(request, 'Turnos/dateSuccess.html', {"mensaje": "Se realizo la reserva correctamente", "context":context})
    return render(request, 'Turnos/asignar_turno.html', {'turno': turno})

# ELIMINAR RESERVA
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
    miTurno = Turno.objects.filter(asignado_a=request.user)
    contador = 0
    for e in Turno.objects.all():
        # print(e.asignado_a)
        if e.asignado_a == request.user:
            print("la puta madre")
            contador += 1
    return render(request ,'Turnos/filtro.html' , {"horaInicio": horaInicio, "contador": contador, 'miTurno': miTurno})
# , {"turno":turno}
def misTurnos(request):
    miTurno = Turno.objects.filter(asignado_a=request.user)
    return render(request, "Turnos/misTurnos.html" , {"miTurno": miTurno})


# CREACION MANUAL DE DIAS EN LA BASE DE DATOS
def prueba(request):
    lista = ["09" , "10", "12", "14"]
    dias = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    fecha_fin = datetime(2024, 12, 31)
    fecha_inicio = datetime(2024, 1, 1)
    for x in range(360):
        hora = fecha_inicio+ timedelta(days=x)
        fecha_formateada = hora.strftime('%Y-%m-%d')
        for x in range(4):
            h=  Turno(fecha=fecha_formateada,hora_inicio=lista[x], hora_fin="20", asignado_a=None, activo=True)
            h.save()
    return redirect('Listar')



#FUNCIONES DE Usuarios
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

def register(request):
    
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
    
        if form.is_valid():            
            username = form.cleaned_data ["username"]
            form.save()
            return render (request, "Turnos/crearUsuario.html",{"mensaje":f"{username}, Usuario Creado :)"})
    
    else: 
        form = UserRegisterForm()
       
    return render (request, "Turnos/crearUsuario.html" , {"form" : form})



class UserList(ListView):

    model = User
    Template_name = "Turnos/user_list.html"

class UserList(ListView):

    model = User
    Template_name = "Turnos/user_list.html"
    
  

class UserDetalle(DetailView):

    model = User
    template_name ="Turnos/detalleUsuario.html"

class UserUpdate(UpdateView):

    model = User
    success_url = "/userlist/"
    fields = ['username', 'email', 'last_name', 'first_name']