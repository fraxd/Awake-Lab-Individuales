from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

#Funcion para evaluar si el usuario es Staff
def isOperador(user):
    return user.groups.filter(name='operador').exists()

def landing_page(request):
    return render(request, 'landing.html')


def crear_usuario(request): 
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            print(user)
            group = form.cleaned_data.get('group')
            group.user_set.add(user)
            return render(request, 'auth/exito.html')
    else:
        form = UsuarioForm()
    
    return render(request, 'auth/crear_usuario.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../../home/')  # Redirecciona a la página de inicio después del inicio de sesión exitoso
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos'
            return render(request, 'auth/login.html', {'error_message': error_message})
    else:
        return render(request, 'auth/login.html')

@login_required
def home_view(request):
    nombre = request.user.first_name or 'Usuario sin nombre definido.'
    if request.user.groups.filter(name='cliente').exists():    
        rol = 'Cliente'
    else:
        rol = 'Operador'
    return render(request, 'private/home.html', {'nombre': nombre, 'rol': rol})

@login_required
@user_passes_test(isOperador)
def user_list(request):
    users = User.objects.all()   
    rol = 'Operador'
    return render(request, 'private/usuarios.html', {'users': users, 'rol': rol})