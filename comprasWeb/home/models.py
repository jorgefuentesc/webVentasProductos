from django.db import models


class Usuario(models.Model):
    usuario_id = models.IntegerField(primary_key=True,default='DEFAULT VALUE')
    run = models.TextField()
    primer_nombre = models.TextField(max_length=40)
    segundo_nombre = models.TextField(max_length=40,default='', blank=True,null=True)
    primer_apellido = models.TextField(max_length=40)
    segundo_apellido = models.TextField(max_length=40,blank=True,null=True)
    correo_electronico = models.TextField(max_length=70) 
    telefono = models.TextField(blank=True, null=True)
    direccion = models.TextField(blank=True,null=True,default='DEFAULT VALUE')
    region = models.TextField(max_length=40,blank=True,null=True,default='DEFAULT VALUE')
    ciudad = models.TextField(max_length=40,blank=True,null=True,default='DEFAULT VALUE')
    fecha_nacimiento = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_vigencia = models.BooleanField(default=True)
    def __str__(self):
        return 'nombre: %s %s' % (self.primer_nombre, self.primer_apellido)
     
class Categoria(models.Model):
    categoria_id = models.IntegerField(primary_key=True, default='DEFAULT VALUE')
    categoria_nombre = models.TextField(max_length=40)
    categoria_fecha_acualizacion = models.TextField()
    categoria_fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria_vigencia = models.BooleanField(default=True)
    def __str__(self):
        return 'id: %s ,%s ' % (self.categoria_id, self.categoria_nombre)

class Producto(models.Model):
    producto_id = models.IntegerField(primary_key=True,default='DEFAULT VALUE')
    codigo = models.IntegerField()
    precio = models.IntegerField()
    prod_nombre = models.TextField(max_length=30)
    prod_descripcion = models.TextField()
    prod_fecha_acualizacion = models.TextField()
    prod_fecha_creacion = models.DateTimeField(auto_now_add=True)
    prod_vigencia = models.BooleanField(default=True)
    categoria_id = models.ForeignKey(Categoria, null=True, blank= True, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario,null=True, blank= True, on_delete=models.CASCADE)
    def __str__(self):
        return 'El nombre del producto es %s y el precio es $ %s' % (self.prod_nombre, self.precio)

class Pedido(models.Model):
    pedido_id = models.IntegerField(primary_key=True, default='DEFAULT VALUE')
    pedido_numero = models.IntegerField()
    pedido_entregado = models.BooleanField(default=True)
    pedido_fecha_actualizacion = models.TextField()
    pedido_fecha_creacion = models.DateTimeField(auto_now_add=True)
    pedido_vigencia = models.BooleanField(default=True)