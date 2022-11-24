from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404,redirect,render
from .forms import LoginUsuario,RegistroUsuario

def login_view(request):
    login_form = LoginUsuario(request.POST or None)
    # login_form2 = LoginUsuario(request.POST)
    # print(login_form2,"222")
    if login_form.is_valid():
        print(request, "noseeewwwwwwwwwwwwwwwwwwwwwwwwww", login_form.cleaned_data.get('email'))
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        # request['email'] = email
        if user is not None:
            login(request, user)           
            messages.success(request, 'Has iniciado sesion correctamente')
            if login:
                request.session['usuario'] = email
                return redirect('home:inicio')
        else:
            messages.warning(request, 'Clave o correo invalidos')
            return redirect('home:inicio')
    messages.error(request, 'Formulario invalido')
    return redirect('home:inicio')

def registro_view(request):
    registro_form = RegistroUsuario(request.POST or None)
    if registro_form.is_valid():
        email = registro_form.cleaned_data.get('email')
        nombres = registro_form.cleaned_data.get('nombres')
        apellidos = registro_form.cleaned_data.get('apellidos')
        password = registro_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email = email,
                nombres = nombres,
                apellidos = apellidos,
                password = make_password(password),
                is_active = True
            )
            login(request,user)
            request.session['usuario'] = email
            return redirect('home:inicio')
        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})

def logout_view(request):
    logout(request)
    return redirect('home:inicio')


# @login_required(login)

            
# Create your views here.
