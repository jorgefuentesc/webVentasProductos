# Generated by Django 4.1 on 2022-11-02 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_usuario_contrasenna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo_electronico',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Correo Electronico'),
        ),
    ]
