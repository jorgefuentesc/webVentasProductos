# Generated by Django 4.1 on 2022-11-01 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usuario_groups_usuario_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contrasenna',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]