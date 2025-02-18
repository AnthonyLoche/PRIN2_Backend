from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import LivrosViewSet, AlunoViewSet, EmprestimosViewSet
router.register(r'livros', LivrosViewSet, basename='livros')
router.register(r'alunos', AlunoViewSet, basename='alunos')
router.register(r'emprestimos', EmprestimosViewSet, basename='emprestimos')

urlpatterns = [
    path('', include(router.urls)),  
]
