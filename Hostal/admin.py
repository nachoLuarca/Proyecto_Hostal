from django.contrib import admin

from .models import Projecto

from .models import Empresa, Solicitante,  Comedor, Menu,Habitacion,Huesped,Orden_Compra,Factura,Detalle_Venta

# Register your models here.

class ProjectoAdmin(admin.ModelAdmin):
    readonly_fields =('creacion', 'actualizacion')


admin.site.register(Projecto, ProjectoAdmin)

# Register your models here.
admin.site.register(Empresa)

admin.site.register(Solicitante)
admin.site.register(Comedor)

admin.site.register(Menu)


admin.site.register(Huesped)

admin.site.register(Orden_Compra)
admin.site.register(Habitacion)
admin.site.register(Factura)

admin.site.register(Detalle_Venta)



