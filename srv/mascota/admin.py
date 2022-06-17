from django.contrib import admin

from mascota.models import PerfilUsuario, Producto, Categoria_Producto, Animal_Producto

# Register your models here.
class admProducto(admin.ModelAdmin):
    list_display=["id","nombre","precio","descripcion"]
    list_editable=["nombre","precio","descripcion"]
    list_filter=["nombre","precio"]
    
    class Meta:
        model=Producto

class admCategoria_Producto(admin.ModelAdmin):
    list_display=["id","categoria"]
    list_editable=["categoria"]

class admAnimal_Producto(admin.ModelAdmin):
    list_display=["id","animal"]
    list_editable=["animal"]

class admPerfilUsuario(admin.ModelAdmin):
    list_display=["nombre_usuario","rut","nombre","apellido"]
    list_editable=["nombre","apellido"]

admin.site.register(Producto,admProducto)
admin.site.register(Categoria_Producto,admCategoria_Producto)
admin.site.register(Animal_Producto,admAnimal_Producto)
admin.site.register(PerfilUsuario,admPerfilUsuario)