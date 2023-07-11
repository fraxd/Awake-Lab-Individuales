import uuid
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class ManejadorUsuario(BaseUserManager):
    def create_user(self, email, nombre, apellidos, password=None, rut=''):
        if not email:
            raise ValueError('El correo electronico es obligatorio')
        if not nombre:
            raise ValueError('El nombre es obligatorio')
        if not apellidos:
            apellidos = ''
        user = self.model(email=self.normalize_email(email), nombre=nombre, apellidos=apellidos, rut = rut)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, nombre, apellidos, password, rut = ''):
        user = self.create_user(email, nombre, apellidos, password, rut)
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, nombre, apellidos, password, rut=''):
        user = self.create_user(email, nombre, apellidos, password, rut)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user





class productor(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    razon_social = models.CharField(max_length=50)
    nombreContacto = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.TextField()
    comuna = models.CharField(max_length=50)


    def __str__(self):
        return self.razon_social

class producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos', null=True)
    stock = models.IntegerField(default=0)
    #productor = models.ForeignKey(productor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class cliente(models.Model):
     direccion = models.CharField( max_length=50)

     def __str__(self) -> str:
         return self.direccion
     


class usuarios(AbstractBaseUser):
    email = models.EmailField(verbose_name='Correo Electronico', max_length=100,unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, default='')
    rut = models.CharField(max_length=10, default='')

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    productor = models.ForeignKey(productor, on_delete=models.SET_NULL, blank=True, null=True)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, null=True, blank=True)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellidos']

    class Meta:
        verbose_name = ('Usuario')
        verbose_name_plural = ('Usuarios')

    def get_full_name(self):
        return self.nombre + ' ' + self.apellidos
    
    def get_short_name(self):
        return self.nombre
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def setCliente(self, cliente):
        self.cliente = cliente
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin   
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_Productor(self):
        if self.productor:
            return True
        return False
    
    @property 
    def is_Cliente(self):
        if self.cliente:
            return True
        return False
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
class Pedido(models.Model):
    productos = models.ManyToManyField(producto, through='DetallePedido')
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_subtotal(self):
        self.subtotal = self.producto.precio * self.cantidad