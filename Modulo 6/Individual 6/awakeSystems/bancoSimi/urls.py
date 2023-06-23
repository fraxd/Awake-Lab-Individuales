from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='Landing Page'),
    
    path('accounts/login/', views.login_view, name='Login'),
    path('users/', views.user_list, name='user_list'),
    path('usersBasico/', views.user_list_basico, name='user_list'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('home/', views.home_view, name='Home'),
    path('home-vip/', views.staff_only_view, name='Home-vip')

]