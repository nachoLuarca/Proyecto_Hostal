from django.db import models

# Create your models here.


class Proveedor(models.Model):
    rut = models.PositiveIntegerField(default=0 )
    nombreEmpresa = models.TextField(max_length=150, unique=True)
    razon = models.CharField(max_length=150, unique=True)
    direction = models.CharField(max_length=150, unique=True)
    correo = models.CharField(max_length=150, unique=True)
    telefono = models.PositiveIntegerField(default=0,)

    def __str__(self):
        return self.nombreEmpresa

    class Meta:
        verbose_name_plural = 'Proveedor'
        ordering = ['id']


class Producto(models.Model):

    prove               = models.ForeignKey (Proveedor, on_delete = models.CASCADE)
    Rut                 = models.PositiveIntegerField(default=0)
    Tipo_producto     = models.CharField(max_length=150, unique=True)
    descripcion      = models.CharField(max_length=150, unique=True)
    cantidad        = models.PositiveIntegerField(default=0)
    fecha_vencimento = models.DateTimeField(auto_now_add=True)
    precio_compra   = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    stock_critico = models.PositiveIntegerField(default=0)
    imagen        = models.ImageField(upload_to="proyecto")
    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['id']


class Empleado(models.Model):


    rut = models.PositiveIntegerField(default=0)
    nombre_Empleado = models.CharField(max_length=150, unique=True)
    cargo = models.CharField(max_length=150, unique=True)
    fecha_contartacion = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateTimeField(auto_now_add=True)
    correo = models.CharField(max_length=150, unique=True)
    contacto = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre_Empleado

    class Meta:
        ordering = ['id']


class ordenPedido(models.Model):

    product = models.ForeignKey(Proveedor, blank=True, null=True, on_delete=models.SET_NULL)
    prove = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.SET_NULL)
    emple = models.ForeignKey(Empleado, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=150, unique=True)
    fecha     = models.DateTimeField(auto_now_add=True )

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['id']

