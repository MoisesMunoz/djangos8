from importlib.resources import path
from unicodedata import name


from mascota.views import listado_productos, agregar_producto, cambiar_password, eliminar_producto, index, listado_usuarios, login, modificar_producto, perfil_usuario, productogato, productoperro, registro, sobrenosotros, carro, conf_pagar
from django.urls import path

urlpatterns = [
    path('',index,name="index"),
    path('sobrenosotros',sobrenosotros,name="sobrenosotros"),
    path('productoperro',productoperro,name="productoperro"),
    path('productogato',productogato,name="productogato"),
    path('login',login,name="login"),
    path('carro',carro,name="carro"),
    path('listado_productos',listado_productos,name="listado_productos"),
    path('conf_pagar',conf_pagar,name="conf_pagar"),
    path('agregar_producto',agregar_producto,name="agregar_producto"),
    path('modificar_producto/<id>',modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>',eliminar_producto,name="eliminar_producto"),
    path('cambiar_password',cambiar_password,name="cambiar_password"),
    path('perfil_usuario',perfil_usuario,name="perfil_usuario"),
    path('registro',registro,name="registro"),
    path('listado_usuarios/',listado_usuarios,name="listado_usuarios"),
]
