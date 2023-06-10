from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('usersBasico/', views.user_list_basico, name='user_list'),
    path('', views.landing_page, name='Landing Page'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),


]