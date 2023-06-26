from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.landing_page, name='Landing Page'),
    
    path('accounts/login/', views.login_view, name='Login'),
    path('accounts/register/', views.crear_usuario, name='Registrarse'),
    path('users/', views.user_list, name='user_list'),
    path('home/', views.home_view, name='Inicio'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]