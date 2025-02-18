from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet, MedicoViewSet, ConsultaViewSet

router = DefaultRouter()

router.register(r'pacientes', PacienteViewSet, basename='pacientes')
router.register(r'medicos', MedicoViewSet, basename='medicos')
router.register(r'consultas', ConsultaViewSet, basename='consultas')

urlpatterns = [
    path('', include(router.urls)),
]