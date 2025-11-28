from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    precio_base = models.PositiveIntegerField()
    imagenes = models.ImageField(upload_to='productos/', null=True, blank=True)

    imagen_1 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen_2 = models.ImageField(upload_to='productos/', null=True, blank=True)
    imagen_3 = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    cantidad_disponible = models.PositiveIntegerField()
    unidad = models.PositiveIntegerField(blank=True)
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
