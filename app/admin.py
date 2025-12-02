from django.contrib import admin
from .models import Producto, Categoria, Insumo , Pedido


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'precio_base', 'imagen_1', 'imagen_2', 'imagen_3','destacado')
    search_fields = ('nombre', 'descripcion')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'cantidad_disponible', 'unidad', 'marca', 'color')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre', 'marca', 'color')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'email', 'telefono', 'red_social', 'producto_referencia', 'plataforma', 'fecha_necesita')
    search_fields = ('nombre_cliente', 'email', 'telefono', 'red_social', 'producto_referencia__nombre', 'plataforma')
