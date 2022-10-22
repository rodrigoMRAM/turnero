from django import forms

class AgregarDias(forms.Form):
    dia = forms.IntegerField()
    hora = forms.IntegerField()
    hora1 = forms.IntegerField()
    hora2 = forms.IntegerField()
    hora3 = forms.IntegerField()
    hora4 = forms.IntegerField()
    clase = forms.IntegerField()