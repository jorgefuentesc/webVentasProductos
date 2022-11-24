from django.contrib import admin
from home.models import Producto,Categoria,Pedido


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


