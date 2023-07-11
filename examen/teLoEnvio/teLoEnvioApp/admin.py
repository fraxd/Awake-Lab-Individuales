from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(producto)
admin.site.register(productor)
admin.site.register(cliente)
admin.site.register(usuarios)