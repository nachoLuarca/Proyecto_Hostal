# Generated by Django 3.2.5 on 2021-07-08 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_rename_nombreempresa_proveedor_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='nombre',
            new_name='nombre_Empleado',
        ),
        migrations.RenameField(
            model_name='proveedor',
            old_name='nombre',
            new_name='nombreEmpresa',
        ),
    ]