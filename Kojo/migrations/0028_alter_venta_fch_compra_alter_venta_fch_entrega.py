# Generated by Django 4.0.5 on 2022-07-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kojo', '0027_venta_iduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fch_compra',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fch_entrega',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]