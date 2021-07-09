from django.contrib import admin

# Register your models here.
from .models import Empleado, Proveedor,  Producto, ordenPedido


# Register your models here.
admin.site.register(Proveedor)

admin.site.register(Empleado)
admin.site.register(ordenPedido)

admin.site.register(Producto)