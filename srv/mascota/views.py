from django.shortcuts import render
from mascota.models import Producto

# Create your views here.
def index(request):
    productos=Producto.objects.all()
    contexto={
        'productos':productos
    }
    return render(request,"mascota/index.html",contexto)

def sobrenosotros(request):
    return render(request,"mascota/sobrenosotros.html")

def productoperro(request):
    productos=Producto.objects.filter(animal="1")
    contexto={
        'productos':productos
    }
    return render(request,"mascota/productoperro.html",contexto)

def productogato(request):
    productos=Producto.objects.filter(animal="2")
    contexto={
        'productos':productos
    }
    return render(request,"mascota/productogato.html",contexto)

def login(request):
    return render(request,"mascota/login.html")

def carro(request):
    return render(request,"mascota/carro.html")

def adminañadymod(request):
    return render(request,"mascota/adminanadymod.html")

def administrador(request):
    productos=Producto.objects.all()
    contexto={
        'productos':productos
    }
    return render(request,"mascota/administrador.html",contexto)

def conf_pagar(request):
    return render(request,"mascota/conf_pagar.html")

def agregar_producto(request):
    return render(request,"mascota/agregar_producto")