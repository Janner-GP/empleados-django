# Generated by Django 4.1.5 on 2023-02-03 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargos', '0001_initial'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fullnameEmpleado',
            field=models.CharField(default=1, max_length=150, verbose_name='Apellido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='apellidoEmpleado',
            field=models.CharField(max_length=150, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargos.cargo', verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombreEmpleado',
            field=models.CharField(max_length=150, verbose_name='Nombre'),
        ),
    ]
