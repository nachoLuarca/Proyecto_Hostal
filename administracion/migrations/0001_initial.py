# Generated by Django 3.2.5 on 2021-07-08 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.PositiveIntegerField(default=0)),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('cargo', models.CharField(max_length=150, unique=True)),
                ('fecha_contartacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateTimeField(auto_now_add=True)),
                ('correo', models.CharField(max_length=150, unique=True)),
                ('contacto', models.PositiveIntegerField(default=0)),
                ('direccion', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.PositiveIntegerField(default=0)),
                ('nombreempresa', models.CharField(max_length=150, unique=True)),
                ('razon', models.CharField(max_length=150, unique=True)),
                ('direction', models.CharField(max_length=150, unique=True)),
                ('correo', models.CharField(max_length=150, unique=True)),
                ('telefono', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.PositiveIntegerField(default=0)),
                ('Tipo_producto', models.CharField(max_length=150, unique=True)),
                ('descripcion', models.CharField(max_length=150, unique=True)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('fecha_vencimento', models.DateTimeField(auto_now_add=True)),
                ('precio_compra', models.DateTimeField(auto_now_add=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('stock_critico', models.PositiveIntegerField(default=0)),
                ('imagen', models.ImageField(upload_to='proyecto')),
                ('prove', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.proveedor')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ordenPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150, unique=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('emple', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.empleado')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.proveedor')),
                ('prove', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.producto')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
