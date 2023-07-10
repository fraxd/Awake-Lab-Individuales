from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    
    path('tareas/crear/', views.editar_tarea_view, name='tarea_crear'),
    path('tareas/<str:tarea_id>/editar/', views.editar_tarea_view, name='editar_tarea'),
    path('tareas/view/<str:tarea_id>', views.tarea_view, name='tarea_view'),
    path('tareas/agregar_observacion/<str:tarea_id>/', views.agregar_observacion, name='agregar_observacion'),
    path('tareas/eliminar_tarea/<str:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tareas/completar_tarea/<str:tarea_id>/', views.completar_tarea, name='completar_tarea'),
    
    
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]