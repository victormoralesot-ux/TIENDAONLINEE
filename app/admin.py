from django.contrib import admin
from .models import Producto, Categoria, Insumo


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'categoria', 'precio_base', 'imagenes')
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
