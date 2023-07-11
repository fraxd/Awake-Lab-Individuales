from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usuarios



class RegistroForm(UserCreationForm):
    direccion = forms.CharField(max_length=100)

    class Meta:
        model = usuarios
        fields = ('email', 'nombre', 'apellidos', 'rut', 'password1', 'password2', 'direccion')
