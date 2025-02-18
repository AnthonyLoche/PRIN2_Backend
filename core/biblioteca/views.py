from rest_framework import viewsets
from .models import Livros, Aluno, Emprestimos
from .serializers import LivrosSerializer, AlunoSerializer, EmprestimosSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class EmprestimosViewSet(viewsets.ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer
