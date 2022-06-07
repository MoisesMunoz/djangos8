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