from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('producto/<int:producto_id>/', views.producto_detalle),
    path('producto/nuevo', views.agregar_producto),
]