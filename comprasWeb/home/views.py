
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator



#

from .forms import CategoriaForm,RegistroUsuarioForm

from .models import Categoria, Producto, Usuario

from django.views.generic import TemplateView, ListView,View
from datetime import datetime
# from django.contrib import messages
# from django.views import View

from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# from django.core.urlresolvers import 
from django.urls import reverse_lazy



class RegistrarUsuario(CreateView):
    model = User
    template_name = "users/usuario/crear_usuario.html"
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('home:inicio')

def nwindex(request):
    
    return render(request, 'home/nwindex.html')
    
    
# Create your views here.

"""
    Orden de secuencia de vistas basadas en clases:

    1.- metodo dispatch: valida la peticion junto con el metodo HTTP en el cual viene
    2.- http_method_not_allowed(): retorna un error cuando se utiliza un methodo HTTP no soportado o definido
    3.- options(): se puede utilizar para el metodo http options siesque se esta usando 

"""




class Inicio(TemplateView):
    template_name = 'home/home/inicio.html'
    """
    solamente se puede utilizar el template name con el templateView para hacer llamado de una poagina/renderizacion
    def get(self, request, *args, **kwargs):
        return render(request, 'home/inicio.html')
    """


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


class ListaCategoria(ListView):
    
    model = Categoria
    template_name = 'home/categoria/categoria.html'
    context_object_name = 'categoria' #retorna como el valor de queryset con el nombre el cual esta definido el cual es 'categoria'
    queryset = Categoria.objects.filter(categoria_vigencia = True)
    """
    Por defecto la funcion ListView retorna el resultado de la consulta, en este caso retorna *queryset*, el contexto que retorna es:
    objet_list
    Igualmente se puede dejar con la funcion get, pero de esta forma se ahorran un par de lineas
    
    def get(self,request,*args,**kwargs):
        categoria = Categoria.objects.filter(categoria_vigencia = True)
         # categoriaProducto = Categoria.objects.filter(Producto.objects.filter(categoria_id=1))
        context = {'categoria':categoria,
                # 'categoriaProducto':categoriaProducto
        }
        return render(request, self.template_name, context)
        
        """
        # def CrearUsuario(request):
#     if request.method == 'POST':
#         usuario_form = UsuarioForm(request.POST)
#         if usuario_form.is_valid():
#             usuario_form.save()
#             return render(request, 'home/inicio.html')
#     else:
#         usuario_form = UsuarioForm() #De esta manera se crea una instancia HTML de los atributos ya creados en el archivo forms de usuarioforms

#     return render(request,'usuario/crear_usuario.html',{'usuario_form': usuario_form})

def crearCategoria(request):
    print("categoriaListaaaaaaaaaaaaaaaa")
    print(request,", requestt")
    now = datetime.now()
    # print(request.method, "metodo actua essss")
    
    name = request.session['usuario']
    # valor2 = request.session.post('username')
    print("categorririri", name)
    # print(valor2,"valor2")
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        print("METIDO EN CREACION")
        if categoria_form.is_valid():
            print("METIDO EN CREACIOssssssssssssssssN")
            categoria_form.save()
            return render(request, 'home/inicio.html')
    else:
        categoria_form = CategoriaForm()
        
        print(now)
        context = {
            'categoria_form':categoria_form,
            
        }
        
    return render(request, 'home/categoria/nueva_categoria.html', {'categoria_form':categoria_form})
    
# def edicarcat(request):
#     nombre = request.POST.get('nombre')
#     print(nombre, "ssssssssssssssssssssssssssssssssssssssssssssssssssss")

    # return JsonResponse(response)
def editarCategoria(request, categoria_id):
    # obtenerDatos = Categoria.objects.filter(categoria_id = categoria_id)
    productoUser = get_object_or_404(Categoria, categoria_id = categoria_id)


    return render(request, 'home/categoria/editar.html', {'categoria':productoUser})
    

def productoCategoria(request,categoria_id):
    
    # productoUser = get_object _or_404(Producto, id=id) #get_object_or_404 sirve como validador en caso de error y tambien retorna un objeto con los parametros requeridos
    productoCategoria = Producto.objects.filter(categoria_id = categoria_id)
    categoriaName = Categoria.objects.get(categoria_id = categoria_id)

    context = {
        'producto':productoCategoria,
        'categoria_name':categoriaName,

    }
    return render(request, 'home/categoria/productos_categoria.html', context)

def nuevaCategoria(request):
    print("HOLAAA")
    valor = request.session.get('username')
    valor2 = request.session['username']
    print(valor)
    print(valor2, "Hello")
    print("catgegogo")

    return render(request, 'home/categoria/nueva_categoria.html')

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
    
    return render(request, 'home/producto/producto.html', context)

def descripcionProducto(request,slug):

    productoUser = get_object_or_404(Producto, slug=slug) #get_object_or_404 sirve como validador en caso de error y tambien retorna un objeto con los parametros requeridos
    # productoUser = Producto.objects.get(slug = slug)
    return render(request, 'home/producto/postProducto.html', {'producto':productoUser})

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
    valor = request.session.get('username')
    valor2 = request.session.get('username')
    print(valor)
    print(valor2, "Hello")
    return render(request, 'home/producto/crear_producto.html')


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

    

