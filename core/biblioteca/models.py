from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano_publicacao}"
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.matricula}"
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

class Emprestimos(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField()

    def __str__(self):
        return f"{self.aluno} - {self.livro} - {self.data_emprestimo} - {self.data_devolucao}"
    
    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"