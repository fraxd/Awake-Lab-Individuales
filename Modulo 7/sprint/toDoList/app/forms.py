from django import forms
from .models import Prioridad, Tarea, Etiqueta
from django.contrib.auth.models import User


class FiltroTareasForm(forms.Form):
    etiqueta = forms.ModelChoiceField(queryset=Etiqueta.objects.all(), required=False)
    estado = forms.ChoiceField(choices=Tarea.OPCIONES_ESTADO, required=False)
    fecha_vencimiento = forms.DateField(required=False)


class TareaForm(forms.ModelForm):
    #estado = forms.ChoiceField(choices=Tarea.OPCIONES_ESTADO, initial='pendiente', required=False)
    #usuario = forms.ModelChoiceField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'etiqueta', 'estado', 'usuario', 'prioridad']
        widgets = {
            'etiqueta': forms.Select(attrs={'class': 'form-control'}),
        }