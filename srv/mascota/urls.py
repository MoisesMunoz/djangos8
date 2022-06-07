from importlib.resources import path
from unicodedata import name


from mascota.views import index, login, productogato, productoperro, sobrenosotros
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('sobrenosotros',sobrenosotros,name="sobrenosotros"),
    path('productoperro',productoperro,name="productoperro"),
    path('productogato',productogato,name="productogato"),
    path('login',login,name="login")
]
