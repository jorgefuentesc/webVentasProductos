
from django.urls import path, include



from .views import inicio,mdl_registro, categorias, productos,descripcionProducto,creacion,productoCategoria,direccionar_producto,crear_producto,nuevaCategoria,crear_categoria,nwindex

# from  django.contrib.auth import views as auth_views

urlpatterns = [
    path('', inicio, name ='inicio'),

    path('nwindex/', nwindex, name='nwindex'),

    #CATEGORIA
    path('categorias/', categorias, name= 'categorias'),
    path('categoriaProduc/<categoria_id>',productoCategoria, name='categoriaProduc'),
    path('nueva_categoria/', nuevaCategoria, name= 'nueva_categoria'),
    path('nueva_categoria/crear_categoria', crear_categoria, name = 'crear_categoria'),
    #PRODUCTO
    path('productos/', productos, name= 'productos'),
    path('crear_producto/', direccionar_producto, name='crear_producto'),
    path('producto/<slug:slug>', descripcionProducto, name='descripcionProducto'),
    path('crear_producto/publicar_prod/', crear_producto, name="publicar_prod/"),
    #--
    # path('crear_usuario/', CrearUsuario, name='crear_usuario'),
    path('mdl-registro/', mdl_registro, name='mdl-registro'),

    # path('test/', testJson, name='test'),
    path('creacion', creacion, name='creacion')
    
]
