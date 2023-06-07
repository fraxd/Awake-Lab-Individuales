from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})