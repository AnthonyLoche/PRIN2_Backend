from rest_framework import serializers
from .models import Livros, Aluno, Emprestimos

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = ['id', 'titulo', 'autor', 'ano_publicacao']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'matricula', 'curso']

class EmprestimosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emprestimos
        fields = ['id', 'aluno', 'livro', 'data_emprestimo', 'data_devolucao']