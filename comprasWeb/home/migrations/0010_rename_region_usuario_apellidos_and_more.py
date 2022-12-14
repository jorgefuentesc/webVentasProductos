# Generated by Django 4.1 on 2022-09-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_producto_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='region',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='segundo_apellido',
            new_name='comuna',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='primer_apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='primer_nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='segundo_nombre',
        ),
        migrations.AddField(
            model_name='usuario',
            name='contrasenna',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombres',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria_fecha_acualizacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria_id',
            field=models.AutoField(default='default', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria_nombre',
            field=models.TextField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pedido_fecha_actualizacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pedido_id',
            field=models.AutoField(default='default', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pedido_numero',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='prod_descripcion',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='prod_fecha_acualizacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='prod_nombre',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='producto_id',
            field=models.AutoField(default='default', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo_electronico',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='run',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario_id',
            field=models.AutoField(default='default', primary_key=True, serialize=False),
        ),
    ]
