from rest_framework import serializers
from .models import Professor, Turma, Aluno

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'disciplina', 'email']

class TurmaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turma
        fields = ['id', 'nome', 'professor', 'horario']

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'matricula', 'curso', 'turma']