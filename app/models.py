from django.db import models
from django.utils import timezone
import uuid

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    
    destacado = models.BooleanField(default=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    precio_base = models.PositiveIntegerField()
    destacado = models.BooleanField(default=False) 

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


class Pedido(models.Model):
    ESTADO_PEDIDO = [
        ('Solicitado', 'Solicitado'),
        ('Aprobado', 'Aprobado'),
        ('En proceso', 'En proceso'),
        ('Realizada', 'Realizada'),
        ('Entregada', 'Entregada'),
        ('Finalizado', 'Finalizado'),
        ('Cancelada', 'Cancelada'),
    ]

    ESTADO_PAGO = [
        ('Pendiente', 'Pendiente'),
        ('Parcial', 'Parcial'),
        ('Pagado', 'Pagado'),
    ]
    
    ESTADO_SOCIAL = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('WhatsApp', 'WhatsApp'),
        ('TikTok', 'TikTok'),
        ('Presencial', 'Presencial'),
        ('Sitio Web', 'Sitio Web'),
    ]

    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    red_social = models.CharField(max_length=20, choices=ESTADO_SOCIAL, default='Sitio Web')
    estado = models.CharField(max_length=20, choices=ESTADO_PEDIDO, default='Solicitado')
    pago = models.CharField(max_length=20, choices=ESTADO_PAGO, default='Pendiente')

    producto_referencia = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True, blank=True
    )
    imagenes_referencia = models.ImageField(upload_to="pedidos/", blank=True, null=True)

    descripcion = models.TextField()
    plataforma = models.CharField(default="pagina web", max_length=50)
    fecha_necesita = models.DateField(blank=True, null=True)

    token_seguimiento = models.CharField(max_length=100, unique=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token_seguimiento:
            self.token_seguimiento = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.nombre_cliente}"
