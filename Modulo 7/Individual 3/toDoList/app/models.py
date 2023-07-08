import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=20)


class Tarea(models.Model):
    OPCIONES_ESTADO = [ # Talvez hacer una clase aparte ?
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO, default='pendiente')
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def mod_estado(self, estado):
        self.estado = estado
        self.save()

    def update_info(self,tituo, descripcion, fecha_vencimiento, etiqueta):
        self.titulo = tituo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.etiqueta = etiqueta
        self.save()

    @classmethod
    def tareas_vencidas(cls):
        return cls.objects.filter(fecha_vencimiento__lt=datetime.date.today())
    
    @classmethod
    def tareas_por_etiqueta(cls, etiqueta):
        return cls.objects.filter(etiqueta=etiqueta)
    
    @classmethod
    def tareas_por_usuario(cls, usuario):
        return cls.objects.filter(usuario=usuario)
