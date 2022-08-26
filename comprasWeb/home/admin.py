from django.contrib import admin
from home.models import Producto,Categoria,Pedido,Usuario


class FormatoUsuarioSTR(admin.ModelAdmin): #Formato para listar en columnas los datos segun nombres que deben ser iguales que en el modelo
    list_display = ('primer_nombre','primer_apellido','correo_electronico','telefono')
    search_fields = ('primer_nombre','primer_apellido','correo_electronico','telefono')
        

class FormatoProductoSTR(admin.ModelAdmin):
    list_display = ('producto_id','prod_nombre','precio','prod_fecha_creacion','categoria_id')
    list_filter = ('prod_nombre','categoria_id',)
    search_fields = ('prod_nombre','precio')

class FormatoCategoriaSTR(admin.ModelAdmin):
    list_display = ('categoria_nombre',)

class FormatoPedidoSTR(admin.ModelAdmin):
    list_display = ('pedido_numero','pedido_vigencia')
    list_filter = ('pedido_fecha_creacion',)
    date_hierarchy = 'pedido_fecha_creacion'

admin.site.register(Producto, FormatoProductoSTR)
admin.site.register(Categoria, FormatoCategoriaSTR)
admin.site.register(Pedido, FormatoPedidoSTR)
admin.site.register(Usuario, FormatoUsuarioSTR)
# Register your models here.
