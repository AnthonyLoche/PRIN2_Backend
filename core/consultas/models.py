from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_consulta = models.DateTimeField()
    descricao = models.TextField()

    def __str__(self):
        return f'{self.data_consulta} - {self.paciente} - {self.medico}'
