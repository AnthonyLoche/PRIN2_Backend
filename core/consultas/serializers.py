from rest_framework import serializers
from .models import Paciente, Medico, Consulta

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'data_nascimento', 'telefone']

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'especialidade', 'crm']

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = ['id', 'paciente', 'medico', 'data_consulta', 'descricao']