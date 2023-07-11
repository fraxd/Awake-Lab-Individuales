from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/login/', views.login_view, name='login'),

    path('cliente/', views.cliente_view, name='cliente'),
]