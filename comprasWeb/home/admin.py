from django.contrib import admin
from home.models import Producto,Categoria,Pedido,Usuario
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UsuarioRerourse(resources.ModelResource):
    class Meta:
        model = Usuario



class UsuarioAmin(ImportExportModelAdmin,admin.ModelAdmin): #Formato para listar en columnas los datos segun nombres que deben ser iguales que en el modelo
    list_display = ('usuario_id','nombres','apellidos','correo_electronico','telefono')
    search_fields = ['nombres','apellidos','correo_electronico','telefono']
    resource_class = UsuarioRerourse

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('producto_id','prod_nombre','precio','prod_fecha_creacion','categoria_id')
    list_filter = ('prod_nombre','categoria_id',)
    search_fields = ('prod_nombre','precio')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria_nombre',)

class PedidoAmin(admin.ModelAdmin):
    list_display = ('pedido_numero','pedido_vigencia')
    list_filter = ('pedido_fecha_creacion',)
    date_hierarchy = 'pedido_fecha_creacion'

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pedido, PedidoAmin)
admin.site.register(Usuario, UsuarioAmin)

