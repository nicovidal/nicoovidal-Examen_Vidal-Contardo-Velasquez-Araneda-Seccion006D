# Generated by Django 4.0.5 on 2022-06-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kojo', '0020_delete_planta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePlanta', models.CharField(max_length=255, verbose_name='Nombre planta')),
                ('nombreCientifico', models.CharField(max_length=255, verbose_name='Nombre cientifico')),
                ('ubicacion', models.CharField(max_length=255, verbose_name='Ubicacion de la plata')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion')),
            ],
        ),
    ]
