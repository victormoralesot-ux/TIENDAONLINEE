from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import api_productos
from app.views import reporte_pedidos
from app.views import pedidos_creados, pedidos_detalle, pedidos_filtrar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('producto/<int:producto_id>/', views.producto_detalle),
    path('producto/nuevo', views.agregar_producto),
    path('formulario', views.agregar_formulario),
    path('pedidos', views.ver_pedidos),
    path("seguimiento/<str:token>/", views.seguimiento_pedido, name="seguimiento_pedido"),
    path('api/productos/', views.api_productos),
    path('api/insumos/', views.insumos_list.as_view()),
    path('api/insumos/<int:pk>/', views.insumos_detail.as_view()), 
    path("reportes/pedidos/", reporte_pedidos, name="reporte_pedidos"),
    path('api/pedidos/', pedidos_creados.as_view()),
    path('api/pedidos/<int:pk>/', pedidos_detalle.as_view()),
    path('api/pedidos/filtrar/', pedidos_filtrar.as_view())


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
