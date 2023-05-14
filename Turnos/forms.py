from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.contrib.auth.models import User


class ToDoForm(forms.Form):
    todo = forms.CharField(widget=forms.TextInput())
    date = forms.DateField(widget=DatePickerInput())
    time = forms.TimeField(widget=TimePickerInput())
    datetime = forms.DateTimeField(widget=DateTimePickerInput())
    class Meta:
         widgets = {
            "date": DatePickerInput(
                attrs={
                    "class": "calendario"
                }
            )
        }

class AgregarDias(forms.Form):
    dia = forms.IntegerField()
    hora = forms.IntegerField()
    hora1 = forms.IntegerField()
    hora2 = forms.IntegerField()
    hora3 = forms.IntegerField()
    hora4 = forms.IntegerField()
    clase = forms.IntegerField()


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'

from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm (UserCreationForm): 
    username = forms.CharField(label="Usuario",max_length=10)
    email = forms.EmailField ()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contraseña", widget=forms.PasswordInput) 
    
    last_name = forms.CharField(label="Nombre")
    first_name= forms.CharField(label="Apellido")

    class Meta: 
      model = User 
      fields = ["username", "email", "password1", "password2", "last_name", "first_name"]
      help_texts = {k:"" for k in fields}