from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"mascota/index.html")

def sobrenosotros(request):
    return render(request,"mascota/sobrenosotros.html")

def productoperro(request):
    return render(request,"mascota/productoperro.html")

def productogato(request):
    return render(request,"mascota/productogato.html")

def login(request):
    return render(request,"mascota/login.html")

def perro1(request):
    return render(request, "mascota/perro1.html")

def perro2(request):
    return render(request, "mascota/perro2.html")

def perro3(request):
    return render(request, "mascota/perro3.html")

def gato1(request):
    return render(request, "mascota/gato1.html")

def gato2(request):
    return render(request, "mascota/gato2.html")

def gato3(request):
    return render(request, "mascota/gato3.html")

def carro(request):
    return render(request,"mascota/carro.html")

def adminañadymod(request):
    return render(request, "mascota/adminañadymod.html")

def admin(request):
    return render (request, "mascota/admin.html")

def conf_pagar(request):
    return render (request, "mascota/conf_pagar.html")