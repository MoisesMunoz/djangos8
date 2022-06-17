from django.contrib import admin

from mascota.models import Producto, Categoria_Producto, Animal_Producto

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria_Producto)
admin.site.register(Animal_Producto)

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