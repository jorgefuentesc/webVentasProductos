
from django.urls import path, include
from .views import inicio,CrearUsuario,mdl_registro, categorias, productos,descripcionProducto,creacion,productoCategoria,direccionar_producto,crear_producto

urlpatterns = [
    path('', inicio, name ='inicio'),

    #CATEGORIA
    path('categorias/', categorias, name= 'categorias'),
    path('categoriaProduc/<categoria_id>',productoCategoria, name='categoriaProduc'),
    #PRODUCTO
    path('productos/', productos, name= 'productos'),
    path('crear_producto', direccionar_producto, name='crear_producto'),
    path('producto/<slug:slug>', descripcionProducto, name='descripcionProducto'),
    path('publicar_prod/', crear_producto, name="publicar_prod"),
    #--
    path('crear_usuario/', CrearUsuario, name='crear_usuario'),
    path('mdl-registro/', mdl_registro, name='mdl-registro'),

    # path('test/', testJson, name='test'),
    path('creacion', creacion, name='creacion')
    
]
