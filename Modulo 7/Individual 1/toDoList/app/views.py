from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

    return render(request, 'private/home.html', {'nombre': nombre})