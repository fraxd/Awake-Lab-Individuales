from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('tareas/view/<str:tarea_id>', views.tarea_view, name='tarea_view'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]