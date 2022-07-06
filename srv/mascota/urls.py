from importlib.resources import path
from unicodedata import name

from mascota.views import PerfilUsuarioViewset, detalle_producto, eliminar_usuario, listado_productos, agregar_producto, eliminar_producto, index, listado_usuarios, login, modificar_producto, perfil_usuario, productogato, productoperro, registro,  sobrenosotros, ProductoViewset
from django.urls import path, include
from rest_framework import routers

router=routers.DefaultRouter()
router.register('producto',ProductoViewset)
router.register('perfilusuario',PerfilUsuarioViewset)

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
    path('api/',include(router.urls))
]
