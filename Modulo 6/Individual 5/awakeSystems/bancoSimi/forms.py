from django import forms
from .models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email',  'saldo', 'sueldo')

    