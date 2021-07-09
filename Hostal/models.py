from django.db import models


from datetime import datetime

# Create your models here.



class Projecto(models.Model):

    titulo        = models.CharField(max_length=150)
    descripcion   = models.TextField(max_length=150)
    imagen        = models.ImageField(upload_to="proyecto")
    link          = models.URLField(null=True, blank=True)
    creacion      = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class meta :
        ordering = ["-creacion"]

    def __str__(self):
        return self.titulo

class Empresa (models.Model):

    rol = models.TextField(max_length=150, unique=True)
    rubro  = models.TextField(max_length=150, unique=True)
    nombre_empresa = models.CharField(max_length=150, unique=True)
    contacto = models.CharField(max_length=150, unique=True)
    correo = models.CharField(max_length=150, unique=True)
    direccion = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre_empresa

    class Meta:


        ordering = ['id']


class Solicitante(models.Model):

    nombre_e = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.SET_NULL)
    rut = models.PositiveIntegerField(default=0)
    nombre = models.CharField(max_length=150, unique=True)
    correo = models.CharField(max_length=150, unique=True)
    telefono = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=150, unique=True)
    mediodepago = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']

class Comedor(models.Model):
    estado = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name_plural = 'Comedores'
        ordering = ['id']

class Menu(models.Model):

    nombre_menu = models.CharField(max_length=150, unique=True)
    tipo_menu = models.CharField(max_length=150, unique=True)
    descripcion = models.CharField(max_length=150, unique=True)
    minuta_diaria = models.CharField(max_length=150, unique=True)
    valor = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre_menu

    class Meta:
        ordering = ['id']


class Habitacion(models.Model):

    estado               = models.BooleanField(default=True)
    tipo                 = models.CharField(max_length=150, unique=True)
    valor_habitacion     = models.PositiveIntegerField(default=0)
    cantidad_camas       = models.PositiveIntegerField(default=0)
    refrescos            = models.CharField(max_length=300, unique=True)
    oficina              = models.BooleanField(default=True,)
    accesorios           = models.CharField(max_length=300, unique=True)
    imagen               = models.ImageField(upload_to="proyecto")
    menu                 = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.tipo

    class Meta:       
        verbose_name_plural = 'Habitaciones'
        ordering = ['id']

class Huesped(models.Model):

    nombre_huesped   = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    habitacion       = models.ForeignKey(Habitacion, blank=True, null=True, on_delete=models.SET_NULL )
    comedor          = models.ForeignKey(Comedor, blank=True, null=True, on_delete=models.SET_NULL)
    contacto         = models.CharField(max_length=150, verbose_name='Telefono', unique=True)
    correo           = models.CharField(max_length=150, verbose_name='Correo', unique=True)
    direccion        = models.CharField(max_length=150, verbose_name='Direccion', unique=True)
    menu             = models.ForeignKey(Menu, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Menu')
    Solicitante      = models.ForeignKey(Solicitante, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Solicitante')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Huespedes'
        ordering = ['id']

class Orden_Compra(models.Model):

    
    solicitante = models.ForeignKey(Solicitante, blank=True, null=True, on_delete=models.SET_NULL )
    descripcion = models.CharField(max_length=150 ,unique=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Ordenes Compras'
        ordering = ['id']

class Factura(models.Model):
    
    Nro         = models.CharField(max_length=150, unique=True)
    rut         = models.CharField(max_length=150, unique=True)
    medio_pago  = models.CharField(max_length=150, unique=True)
    detalle     = models.CharField(max_length=150, unique=True)
    fecha        = models.DateField(default=datetime.now)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.details

    class Meta:
        verbose_name_plural = 'Facturas'

        ordering = ['id']

class Detalle_Venta(models.Model):

    orden            = models.ForeignKey(Orden_Compra, blank=True, null=True, on_delete=models.SET_NULL)
    huesped          = models.ForeignKey(Huesped, blank=True, null=True, on_delete=models.SET_NULL)
    Factura          = models.ForeignKey(Factura, blank=True, null=True, on_delete=models.SET_NULL)
    descripcion      = models.CharField(max_length=150, unique=True )
    precio_total     = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    Sub_total        = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.orden

    class Meta:
        verbose_name_plural = 'Detalles Ventas'
        ordering = ['id']


    






