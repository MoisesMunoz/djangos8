from importlib.resources import path
from unicodedata import name


from mascota.views import administrador, crear_usuario, eliminar_usuario, index, listado_usuarios, login, modificar_usuario, productogato, productoperro, sobrenosotros, perro1, perro2, perro3, gato1, gato2, gato3, carro, adminañadymod, conf_pagar
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
    path('administrador',administrador,name="administrador"),
    path('adminanadymod',adminañadymod,name="adminanadymod"),
    path('conf_pagar',conf_pagar,name="conf_pagar"),
    path('crear_usuario',crear_usuario,name="crear_usuario"),
    path('eliminar_usuario',eliminar_usuario,name="eliminar_usuario"),
    path('listado_usuarios',listado_usuarios,name="listado_usuarios"),
    path('modificar_usuario',modificar_usuario,name="modificar_usuario")
]
