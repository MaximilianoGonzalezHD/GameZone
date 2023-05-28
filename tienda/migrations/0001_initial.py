# Generated by Django 4.2.1 on 2023-05-28 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rolr', models.AutoField(primary_key=True, serialize=False)),
                ('nombrer', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id_seccions', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('id_juego', models.AutoField(primary_key=True, serialize=False)),
                ('nombrev', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=300)),
                ('precio', models.FloatField(verbose_name='Precio de videojuegos')),
                ('imagenv', models.ImageField(blank=True, upload_to='ImagenVideojuegos', verbose_name='Imagen de videojuegos')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuariou', models.AutoField(primary_key=True, serialize=False)),
                ('emailu', models.CharField(max_length=20)),
                ('nombre_usuariou', models.CharField(max_length=15)),
                ('contrasenau', models.CharField(max_length=15)),
                ('nombreu', models.CharField(blank=True, max_length=30)),
                ('imagenu', models.ImageField(blank=True, upload_to='ImagenUser', verbose_name='Imagen De Usuario')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Detallesc',
            fields=[
                ('id_detallesc', models.AutoField(primary_key=True, serialize=False)),
                ('subtotal', models.FloatField(verbose_name='Subtotal de la compra')),
                ('cantidad', models.IntegerField(verbose_name='cantidad de productos')),
                ('id_juego', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.videojuegos')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_comprac', models.AutoField(primary_key=True, serialize=False)),
                ('fechac', models.DateField(verbose_name='Fecha de compra')),
                ('rutc', models.CharField(max_length=16)),
                ('totalc', models.IntegerField(verbose_name='Total De la Compra')),
                ('id_detalles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.detallesc')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.usuario')),
            ],
        ),
    ]
