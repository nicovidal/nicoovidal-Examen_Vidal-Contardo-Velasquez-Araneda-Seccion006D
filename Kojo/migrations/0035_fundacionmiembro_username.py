# Generated by Django 4.0.5 on 2022-07-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kojo', '0034_fundacionmiembro_delete_fundacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundacionmiembro',
            name='userName',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]