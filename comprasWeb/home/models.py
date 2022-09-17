
from django.db import models


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    run = models.CharField(max_length=20,blank=True,null=True)
    nombres = models.CharField(max_length=220,blank=True,null=True)
    apellidos = models.CharField(max_length=220,blank=True,null=True)
    fecha_nacimiento = models.CharField(max_length=220,blank=True,null=True)
    usuario = models.CharField(max_length=220, blank=True,null=True)
    contrasenna = models.CharField(max_length=220,blank=True,null=True)
    correo_electronico = models.CharField(max_length=220,blank=True,null=True) 
    telefono = models.CharField(max_length=20,blank=True, null=True)
    ciudad = models.CharField(max_length=220,blank=True,null=True)
    comuna = models.CharField(max_length=220,blank=True,null=True)
    direccion = models.CharField(max_length=220,blank=True,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_vigencia = models.BooleanField(default=True)
    def __str__(self):
        return 'nombre: %s %s' % (self.nombres, self.apellidos)
     
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.TextField(max_length=40,blank=True,null=True)
    categoria_fecha_acualizacion = models.TextField(blank=True, null=True)
    categoria_fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria_vigencia = models.BooleanField(default=True)
    def __str__(self):
        return 'id: %s ,%s ' % (self.categoria_id, self.categoria_nombre)

class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    precio = models.IntegerField(blank=True,null=True)
    prod_nombre = models.TextField(max_length=120, blank=True,null=True)
    prod_descripcion = models.TextField(max_length=400,blank=True,null=True)
    prod_imagen = models.URLField(max_length=255,blank=True, null=True)
    slug = models.CharField(max_length=60, blank=True, null=True)
    prod_fecha_acualizacion = models.TextField(blank=True, null=True)
    prod_fecha_creacion = models.DateTimeField(auto_now_add=True)
    prod_vigencia = models.BooleanField(default=True)
    categoria_id = models.ForeignKey(Categoria, blank=True,null=True, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario,blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return 'El nombre del producto es %s y el precio es $ %s id fk: %s' % (self.prod_nombre, self.precio, self.categoria_id)

class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True,default='default')
    pedido_numero = models.IntegerField(blank=True,null=True)
    pedido_entregado = models.BooleanField(default=True)
    pedido_fecha_actualizacion = models.TextField(blank=True,null=True)
    pedido_fecha_creacion = models.DateTimeField(auto_now_add=True)
    pedido_vigencia = models.BooleanField(default=True)