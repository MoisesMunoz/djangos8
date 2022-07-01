from django.shortcuts import render, redirect, get_object_or_404
from mascota.carro import Carro
from mascota.models import PerfilUsuario, Producto
from mascota.forms import PerfilUsuarioForm, ProductoForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required
from rest_framework import viewsets
from .serializers import PerfilUsuarioSerializer, ProductoSerializer

# Create your views here.
class ProductoViewset(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer

    def get_queryset(self):
        productos=Producto.objects.all()
        nombre=self.request.GET.get("nombre")
        if nombre:
            productos=productos.filter(nombre__contains=nombre)
        return productos

class PerfilUsuarioViewset(viewsets.ModelViewSet):
    queryset=PerfilUsuario.objects.all()
    serializer_class=PerfilUsuarioSerializer

def index(request):
    productos=Producto.objects.all()
    usuarios=PerfilUsuario.objects.all()
    contexto={
        'productos':productos,
        'usuarios':usuarios
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

@login_required()
def listado_productos(request):
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
    return render(request,"mascota/listado_productos.html",contexto)

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
            return redirect(to="listado_productos")
        contexto["form"]=formulario

    return render(request,"mascota/modificar_producto.html",contexto)

def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listado_productos")

def perfil_usuario(request):
    
    form=PerfilUsuarioForm(request.POST or None)
    
    contexto={
        "form":form
    }
    if request.method=="POST":
        form=PerfilUsuarioForm(data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            perfil=PerfilUsuario()
            perfil.rut=datos.get("rut")
            perfil.nombre=datos.get("nombre")
            perfil.apellido=datos.get("apellido")
            perfil.nombre_usuario=request.user.username
            perfil.save()
            
            return redirect(to="index")

    return render(request,"registration/perfil_usuario.html",contexto)

def registro(request):
    form=UserCreationForm(request.POST or None)
    contexto={
        "form":form
    }
    
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            credenciales=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
            login(request,credenciales)
            return redirect(to="perfil_usuario")
    
    return render(request,"registration/registro.html",contexto)

def listado_usuarios(request):
    usuarios=PerfilUsuario.objects.all()

    page=request.GET.get('page',1)

    try:
        paginator=Paginator(usuarios, 6)
        usuarios=paginator.page(page)
    except:
        raise Http404

    contexto={
        'entity':usuarios,
        'paginator':paginator
    }
    return render(request,"mascota/listado_usuarios",contexto)

def detalle_producto(request,id):
    if Producto.objects.filter(id=id).exists():
        producto=Producto.objects.get(id=id)
        contexto={
            "producto":producto
        }
    return render(request,"mascota/detalle_producto.html",contexto)

def eliminar_usuario(request,id):
    usuario=get_object_or_404(PerfilUsuario,id=id)
    usuario.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listado_usuarios")

def ver_carro(request):
    return render(request,'mascota/ver_carro.html',{'carro': request.session['carro']})

def agregar_producto_carro(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect(to="/ver_carro")

def eliminar_producto_carro(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect(to="/ver_carro")


def restar_producto_carro(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect(to="/ver_carro")

def vaciar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(to="/ver_carro")


def comprar(request):
    messages.success(request, 'Gracias por su Compra!!')
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('/')