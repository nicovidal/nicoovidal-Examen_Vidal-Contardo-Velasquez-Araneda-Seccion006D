# Generated by Django 4.0.5 on 2022-06-22 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kojo', '0014_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
