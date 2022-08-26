from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'home/inicio.html')

def busquedaProd(request):
    mensaje = "buscado: %r" %request.GET["bsq"]
    return HttpResponse(mensaje)