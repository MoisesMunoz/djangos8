from importlib.resources import path
from unicodedata import name


from mascota.views import agregar_producto_carro, comprar, detalle_producto, eliminar_producto_carro, eliminar_usuario, listado_productos, agregar_producto, eliminar_producto, index, listado_usuarios, login, modificar_producto, perfil_usuario, productogato, productoperro, registro, restar_producto_carro, sobrenosotros, vaciar_carro, ver_carro
from django.urls import path
from rest_framework import routers

routers = routers.DefaultRouter()
router.register('producto', ProductoView)


urlpatterns = [
    path('',index,name="index"),
    path('sobrenosotros',sobrenosotros,name="sobrenosotros"),
    path('productoperro',productoperro,name="productoperro"),
    path('productogato',productogato,name="productogato"),
    path('login',login,name="login"),
    path('listado_productos',listado_productos,name="listado_productos"),
    path('agregar_producto',agregar_producto,name="agregar_producto"),
    path('modificar_producto/<id>',modificar_producto,name="modificar_producto"),
    path('eliminar_producto/<id>',eliminar_producto,name="eliminar_producto"),
    path('perfil_usuario',perfil_usuario,name="perfil_usuario"),
    path('registro',registro,name="registro"),
    path('listado_usuarios/',listado_usuarios,name="listado_usuarios"),
    path('detalle_producto/<id>',detalle_producto,name="detalle_producto"),
    path('eliminar_usuario/<id>',eliminar_usuario,name="eliminar_usuario"),
    path('ver_carro',ver_carro,name="ver_carro"),
    path('agregar_producto_carro/<producto_id>',agregar_producto_carro,name="agregar_producto_carro"),
    path('eliminar_producto_carro/<producto_id>',eliminar_producto_carro,name="eliminar_producto_carro"),
    path('restar_producto_carro/<producto_id>',restar_producto_carro,name="restar_producto_carro"),
    path('vaciar_carro',vaciar_carro,name="vaciar_carro"),
    path('comprar',comprar,name="comprar"),
]
