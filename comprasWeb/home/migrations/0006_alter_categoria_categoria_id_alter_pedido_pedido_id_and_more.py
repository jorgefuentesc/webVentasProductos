# Generated by Django 4.1 on 2022-08-26 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_usuario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria_id',
            field=models.AutoField(default='DEFAULT VALUE', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pedido_id',
            field=models.AutoField(default='DEFAULT VALUE', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_id',
            field=models.AutoField(default='DEFAULT VALUE', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_id',
            field=models.AutoField(default='DEFAULT VALUE', primary_key=True, serialize=False),
        ),
    ]
