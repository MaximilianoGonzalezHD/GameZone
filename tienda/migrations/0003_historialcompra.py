# Generated by Django 4.2.1 on 2023-07-10 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_usuario_imagenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.compra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.usuario')),
            ],
        ),
    ]
