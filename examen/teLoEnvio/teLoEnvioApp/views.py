from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import cliente, usuarios
from .forms import RegistroForm


def index_view(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            direccion = form.cleaned_data['direccion']
            clienteVar = cliente(direccion=direccion)
            user = form.save()
            clienteVar.save()
            user.setCliente(clienteVar)
            user.save()

            return redirect('login')  # Reemplaza 'home' con la URL de tu página principal
        else: 
            mensaje = 'Error.' + ' ' + form.errors
            messages.error(request, mensaje)

    else:
        form = RegistroForm()

    return render(request, 'auth/register.html', {'form': form})
# crea un login view 


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('admin')
            if user.is_Productor:
                return redirect('productor')
            if user.is_Cliente:
                return redirect('cliente')
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo nuevamente.')

    return render(request, 'auth/login.html')

@login_required
def cliente_view(request):
    return render(request, 'clientes/home.html')

@login_required
def home_view(request):
    return render(request, 'home.html')