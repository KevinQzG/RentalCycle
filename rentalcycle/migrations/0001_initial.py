# Generated by Django 3.2.8 on 2023-05-16 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id_bicicleta', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('modelo_bicicleta', models.CharField(max_length=15)),
                ('marca_bicicleta', models.CharField(max_length=10)),
                ('estado_bicicleta', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id_campus', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campus', models.CharField(max_length=20, verbose_name='Campus')),
                ('direccion_campus', models.CharField(max_length=15, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('primer_nombre_empleado', models.CharField(max_length=20)),
                ('primer_apellido_empleado', models.CharField(max_length=20)),
                ('cargo_empleado', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('codigo_promocion', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion_promocion', models.CharField(max_length=25)),
                ('id_encargado', models.ForeignKey(db_column='id_encargado', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('codigo_mantenimiento', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha_mantenimiento', models.DateField()),
                ('descripcion_mantenimiento', models.CharField(max_length=25)),
                ('id_bicicleta', models.ForeignKey(db_column='id_bicicleta', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.bicicleta')),
                ('id_empleado', models.ForeignKey(db_column='id_empleado', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre_estudiante', models.CharField(max_length=20, verbose_name='Primer Nombre')),
                ('primer_apellido_estudiante', models.CharField(max_length=20, verbose_name='Primer Apellido')),
                ('carrera_estudiante', models.CharField(max_length=25, verbose_name='Carrera')),
                ('id_campus', models.ForeignKey(db_column='id_campus', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.campus', verbose_name='Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('codigo_alquiler', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_alquiler', models.DateTimeField()),
                ('fecha_prevista', models.DateField()),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('dias_retraso', models.IntegerField(blank=True, null=True)),
                ('id_bicicleta', models.ForeignKey(db_column='id_bicicleta', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.bicicleta')),
                ('id_estudiante', models.ForeignKey(db_column='id_estudiante', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='CampusPromocion',
            fields=[
                ('id_campus', models.OneToOneField(db_column='id_campus', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='rentalcycle.campus')),
                ('inicio_promocion', models.DateField()),
                ('fin_promocion', models.DateField()),
                ('codigo_promocion', models.ForeignKey(db_column='codigo_promocion', on_delete=django.db.models.deletion.DO_NOTHING, to='rentalcycle.promocion')),
            ],
        ),
    ]