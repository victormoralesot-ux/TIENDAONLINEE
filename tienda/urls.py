from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import api_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('producto/<int:producto_id>/', views.producto_detalle),
    path('producto/nuevo', views.agregar_producto),
    path('formulario', views.agregar_formulario),
    path('pedidos', views.ver_pedidos),
    path("seguimiento/<str:token>/", views.seguimiento_pedido, name="seguimiento_pedido"),
    path('api/productos/', views.api_productos),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
