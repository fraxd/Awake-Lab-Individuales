from .forms import FiltroTareasForm, TareaForm
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Tarea

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
    form = FiltroTareasForm(request.GET or None)
    nombre = request.user.first_name or 'Usuario sin nombre definido.'
    tareas = Tarea.objects.filter(usuario=request.user.id).order_by('fecha_vencimiento')
    if form.is_valid():
        etiqueta = form.cleaned_data.get('etiqueta')
        estado = form.cleaned_data.get('estado')
        fecha_vencimiento = form.cleaned_data.get('fecha_vencimiento')
        if estado:
            tareas = tareas.filter(estado=estado)
        if etiqueta:
            tareas = tareas.filter(etiqueta=etiqueta)
        if fecha_vencimiento:
            tareas = tareas.filter(fecha_vencimiento=fecha_vencimiento)

    return render(request, 'private/home.html', {'nombre': nombre, 'tareas': tareas, 'form':form})

@login_required
def tarea_view(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    return render(request, 'private/ver_tarea.html', {'tarea': tarea})

@login_required
def editar_tarea_view(request, tarea_id=None):
    tarea = None
    if tarea_id:
        tarea = get_object_or_404(Tarea, id=tarea_id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        print(form.errors)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.estado = 'pendiente'
            tarea.save()
            return redirect('home')
        else:
            error = 'El Formulario esta incompleto o no es valido.'
            return render(request, 'private/editar_tarea.html', {'form': form, 'error': error, 'tarea': tarea})
    else:
        form = TareaForm()
    return render(request, 'private/editar_tarea.html', {'form': form, 'tarea': tarea})