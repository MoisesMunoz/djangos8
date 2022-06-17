from django.shortcuts import render, redirect, get_object_or_404
from mascota.models import Producto
from mascota.forms import ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

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

    page=request.GET.get('page',1)

    try:
        paginator=Paginator(productos, 6)
        productos=paginator.page(page)
    except:
        raise Http404

    contexto={
        'entity':productos,
        'paginator':paginator
    }
    return render(request,"mascota/administrador.html",contexto)

def conf_pagar(request):
    return render(request,"mascota/conf_pagar.html")

def agregar_producto(request):
    contexto={
        'form':ProductoForm()
    }

    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Registrado")
        else:
            contexto["form"]=formulario

    return render(request,"mascota/agregar_producto.html",contexto)

def modificar_producto(request,id):
    
    producto=get_object_or_404(Producto, id=id)
    
    contexto={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="administrador")
        contexto["form"]=formulario

    return render(request,"mascota/modificar_producto.html",contexto)

def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="administrador")