# Generated by Django 4.0.5 on 2022-07-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kojo', '0029_fundacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundacion',
            name='idMiembro',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID_Miem'),
        ),
    ]
