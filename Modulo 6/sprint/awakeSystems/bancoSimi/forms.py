from django import forms
from django.contrib.auth.models import User, Group

class UsuarioForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'group')
