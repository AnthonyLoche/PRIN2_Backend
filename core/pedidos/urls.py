from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import PedidoViewSet, ClientesViewSet, ItemPedidoViewSet

router.register(r'pedidos', PedidoViewSet, basename='pedidos')
router.register(r'clientes', ClientesViewSet, basename='clientes')
router.register(r'itenspedido', ItemPedidoViewSet, basename='itenspedido')

urlpatterns = [
    path('', include(router.urls)),  
]