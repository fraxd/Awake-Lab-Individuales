from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UsuarioForm


# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})

def user_list_basico(request):
    users = User.objects.all()
    return render(request, 'userBasicos.html', {'users': users})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Guardar los datos del formulario en la base de datos u otra lógica
            form.save()
            return render(request, 'exito.html')
    else:
        form = UsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})