from importlib.resources import path
from unicodedata import name


from mascota.views import administrador, agregar_producto, index, login, productogato, productoperro, sobrenosotros, carro, adminañadymod, conf_pagar
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('sobrenosotros',sobrenosotros,name="sobrenosotros"),
    path('productoperro',productoperro,name="productoperro"),
    path('productogato',productogato,name="productogato"),
    path('login',login,name="login"),
    path('carro',carro,name="carro"),
    path('administrador',administrador,name="administrador"),
    path('adminanadymod',adminañadymod,name="adminanadymod"),
    path('conf_pagar',conf_pagar,name="conf_pagar"),
    path('agregar_producto',agregar_producto,name="agregar_producto"),
]
