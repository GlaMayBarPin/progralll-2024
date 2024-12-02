# Generated by Django 5.1.1 on 2024-11-17 00:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_delete_extras_tipo_ingrediente_mensaje_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_ingrediente',
            name='mensaje',
        ),
        migrations.RemoveField(
            model_name='tipo_ingrediente',
            name='multiple',
        ),
        migrations.AddField(
            model_name='producto_tipo_ingrediente',
            name='mensaje',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='producto_tipo_ingrediente',
            name='multiple',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 18, 30, 18, 588808)),
        ),
        migrations.AlterField(
            model_name='descuento',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 16, 18, 30, 18, 588808)),
        ),
    ]
