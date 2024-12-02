# Generated by Django 5.1.1 on 2024-09-24 23:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('correo', models.EmailField(max_length=200, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=9)),
                ('contraseña', models.CharField(max_length=128)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('indicaciones', models.TextField(null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
                'db_table': 'direcciones',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('usuarios', models.ManyToManyField(related_name='roles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'db_table': 'roles',
            },
        ),
    ]
