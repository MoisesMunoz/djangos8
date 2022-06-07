from importlib.resources import path
from unicodedata import name


from mascota.views import index, login, productogato, productoperro, sobrenosotros, perro1, perro2, perro3, gato1, gato2, gato3, carro, adminañadymod, admin, conf_pagar
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('sobrenosotros',sobrenosotros,name="sobrenosotros"),
    path('productoperro',productoperro,name="productoperro"),
    path('productogato',productogato,name="productogato"),
    path('login',login,name="login"),
    path('perro1',perro1,name="perro1"),
    path('perro2',perro2,name="perro2"),
    path('perro3',perro3,name="perro3"),
    path('gato1',gato1,name="gato1"),
    path('gato2',gato2,name="gato2"),
    path('gato3',gato3,name="gato3"),
    path('carro',carro,name="carro"),
    path('admin',admin,name="admin"),
    path('adminañadymod',adminañadymod,name="adminañadymod"),
    path('conf_pagar',conf_pagar,name="conf_pagar")
    
]
