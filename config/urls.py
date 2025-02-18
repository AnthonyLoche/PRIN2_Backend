from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from core.pedidos.views import PedidoViewSet, ItemPedidoViewSet, ClientesViewSet
from core.pedidos.urls import router as pedidos_router

router = DefaultRouter()
router.registry.extend(pedidos_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
