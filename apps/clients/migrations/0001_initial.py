# Generated by Django 4.0.4 on 2023-06-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('email', models.CharField(max_length=100)),
                ('birtday', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fecha de nacimiento')),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
