from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import User as usuarioBasico
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test

#Funcion para evaluar si el usuario es Staff
def is_staff_user(user):
    return user.is_authenticated and user.is_staff

# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})

def user_list_basico(request):
    usuariosBasicos = usuarioBasico.objects.all()
    return render(request, 'userBasicos.html', {'users': usuariosBasicos})

def crear_usuario(request): 
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('Es valido')
            user = form.save()
            print(user)
            group = form.cleaned_data.get('group')
            print('---------------------')
            print(group)
            group.user_set.add(user)
            return render(request, 'exito.html')
    else:
        form = UsuarioForm()
    
    return render(request, 'crear_usuario.html', {'form': form})

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


def logout_view(request):
    #logout(request)
    return redirect('login')  

@login_required
def home_view(request):
    nombre = request.user.first_name or 'Usuario sin nombre definido.'

    return render(request, 'private/home.html', {'nombre': nombre})

@user_passes_test(is_staff_user)
def staff_only_view(request):
    return render(request, 'private/home-vip.html')