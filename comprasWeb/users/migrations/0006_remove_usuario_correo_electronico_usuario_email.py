# Generated by Django 4.1 on 2022-11-11 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_usuario_correo_electronico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo_electronico',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email'),
        ),
    ]
