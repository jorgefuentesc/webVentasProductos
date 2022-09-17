
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Categoria, Producto, Usuario
# from django.contrib import messages
# from django.views import View




def nwindex(request):
    return render(request, 'home/nwindex.html')
    
# Create your views here.
def inicio(request):
    # queryset = request.GET.get('buscar')
    # print(queryset, "ssssss")
    return render(request, 'home/inicio.html')



# class ClassName(request):
#     def get(self,request):
#         return super(ClassName).__init__()
#     def post(self,request):
#         pass
        

# def CrearUsuario(request):
#     if request.method == 'POST':
#         usuario_form = UsuarioForm(request.POST)
#         if usuario_form.is_valid():
#             usuario_form.save()
#             return render(request, 'home/inicio.html')
#     else:
#         usuario_form = UsuarioForm() #De esta manera se crea una instancia HTML de los atributos ya creados en el archivo forms de usuarioforms

#     return render(request,'usuario/crear_usuario.html',{'usuario_form': usuario_form})




    


def redirecInicio(request):

    return render(request, 'modal/mdl-inicio.html')


def mdl_registro(request):
    
    if request.method == 'POST':

        run = request.POST.get('run')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        correo_electronico = request.POST.get('correo_electronico')
        telefono = request.POST.get('telefono')
        ciudad = request.POST.get('ciudad')
        comuna = request.POST.get('comuna')
        fecha_nac = request.POST.get('fecha_nac')
        sexo = request.POST.get('sexo')
 

        usuario = Usuario.objects.create(
            run = run,
            nombres = nombre,
            apellidos = apellido,
            fecha_nacimiento = fecha_nac,
            usuario = usuario,
            contrasenna = contrasena,
            correo_electronico = correo_electronico,
            telefono = telefono,
            ciudad = ciudad,
            comuna = comuna,
            direccion = sexo,
        )
        usuario.save()
        print("creacion exitosa")
    response={
        'estado':1
    }

    return JsonResponse(response)

#CATEGORIA
""""CATEGORIA"""
def categorias(request):

    categoria = Categoria.objects.filter(categoria_vigencia = True)
    # categoriaProducto = Categoria.objects.filter(Producto.objects.filter(categoria_id=1))
    context = {'categoria':categoria,
                # 'categoriaProducto':categoriaProducto
    }
    return render(request, 'categoria/categoria.html', context)

def productoCategoria(request,categoria_id):
    
    # productoUser = get_object _or_404(Producto, id=id) #get_object_or_404 sirve como validador en caso de error y tambien retorna un objeto con los parametros requeridos
    productoCategoria = Producto.objects.filter(categoria_id = categoria_id)
    categoriaName = Categoria.objects.get(categoria_id = categoria_id)

    context = {
        'producto':productoCategoria,
        'categoria_name':categoriaName,

    }
    return render(request, 'categoria/productos_categoria.html', context)

def nuevaCategoria(request):
    valor = request.session.get('username')
    print(valor)
    print("catgegogo")

    return render(request, 'categoria/nueva_categoria.html')

def crear_categoria(request): 
    print("lactm")   
    nombre = request.POST.get('gte_nombre')
    fecha = request.POST.get('ctg_fecha_act')
    categoria = Categoria.objects.create(
        categoria_nombre = nombre,
        categoria_fecha_acualizacion = fecha
    )
    categoria.save()
    print("Exito")
    response = {
        "estado":1,
    }       
    return JsonResponse(response)
    

#PRODUCTO
"""""PRODUCTO"""
def productos(request):
    queryset = request.GET.get('buscar')
    
    if queryset:
        prodrelated = Producto.objects.filter( 
            Q(prod_nombre__icontains = queryset, prod_vigencia = True)
            # Q(precio__gte = queryset, prod_vigencia = True)
        )
        print("Existebuscar")
    else:
        productos = Producto.objects.filter(prod_vigencia = True)
        prodrelated = Producto.objects.all().select_related("categoria_id")
    paginator = Paginator(prodrelated,4)
    page = request.GET.get('page')
    prodrelated = paginator.get_page(page)
    context={
        'productos':prodrelated
    }
    
    return render(request, 'producto/producto.html', context)

def descripcionProducto(request,slug):

    productoUser = get_object_or_404(Producto, slug=slug) #get_object_or_404 sirve como validador en caso de error y tambien retorna un objeto con los parametros requeridos
    # productoUser = Producto.objects.get(slug = slug)
    return render(request, 'producto/postProducto.html', {'producto':productoUser})

def crear_producto(request):
    
    print("reciii")
    nombre = request.POST.get('nombre')
    precio = request.POST.get('precio')
    descripcion = request.POST.get('descripcion')
    slug = request.POST.get('slug')

    print(nombre, precio, descripcion, slug)

    response = {
        'estado': 1
    }

    return JsonResponse(response)

def direccionar_producto(request):

    return render(request, 'producto/crear_producto.html')


# def testJson(request):
#     try:
#         testProduc = list(Producto.objects.values())
#         print("ss",request.GET.get('oww'))
#         print(request)
        
#         if (len(testProduc) > 0):
#             data = {'messaje':"Succes", 'producto':testProduc}
#         else:
#             data = {'messaje':"Not Found"}
#     except Exception as identifier: 
#         print("sucedio algo malo uwu")
#         data = {
#             'estado': 0
#         }
#     return JsonResponse(data)
    

def creacion(request):
    return render(request, 'home/creacion.html')

    

