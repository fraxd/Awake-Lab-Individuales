from django.shortcuts import render
# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')

def usuariosRegistrados(request):
    return render(request, 'usuariosRegistrados.html')
