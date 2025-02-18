from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from core.biblioteca.urls import router as biblioteca_router
from core.pedidos.urls import router as pedidos_router
from core.consultas.urls import router as consultas_router
from core.turmas.urls import router as turmas_router

router = DefaultRouter()
router.registry.extend(biblioteca_router.registry)
router.registry.extend(pedidos_router.registry)
router.registry.extend(consultas_router.registry)
router.registry.extend(turmas_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
