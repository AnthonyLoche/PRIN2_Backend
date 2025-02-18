from django.core.management.base import BaseCommand
import random
from faker import Faker
from datetime import datetime
from django.utils import timezone  
from random import randint
from core.pedidos.models import Clientes, Pedidos, ItensPedido
from core.biblioteca.models import Aluno, Livros, Emprestimos
from core.consultas.models import Medico, Paciente, Consulta
from core.turmas.models import Professor, Turma, Aluno as AlunoTurma

fake = Faker('pt_BR')

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Iniciando a população do banco de dados...'))

        # Clientes
        self.stdout.write(self.style.SUCCESS('Populando Clientes...'))
        clientes = [
            Clientes.objects.create(
                nome=fake.name(),
                email=fake.email(),
                telefone=fake.phone_number()
            ) for _ in range(10)
        ]
        self.stdout.write(self.style.SUCCESS('Clientes populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando Pedidos...'))
        pedidos = [
            Pedidos.objects.create(
                cliente=random.choice(clientes),
                data=fake.date_time_this_year(),
                total=round(random.uniform(50, 1000), 2)
            ) for _ in range(20)
        ]
        self.stdout.write(self.style.SUCCESS('Pedidos populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando ItensPedido...'))
        for _ in range(30):
            ItensPedido.objects.create(
                pedido=random.choice(pedidos),
                produto=fake.word(),
                preco=round(random.uniform(10, 500), 2),
                quantidade=random.randint(1, 5)
            )
        self.stdout.write(self.style.SUCCESS('ItensPedido populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando Alunos e Livros...'))
        alunos = [
            Aluno.objects.create(
                nome=fake.name(),
                curso=fake.word(),
                matricula=fake.unique.random_number(digits=6)
            ) for _ in range(10)
        ]
        livros = [
            Livros.objects.create(
                titulo=fake.sentence(nb_words=3),
                autor=fake.name(),
                ano_publicacao=randint(1900, 2024)
            ) for _ in range(10)
        ]
        self.stdout.write(self.style.SUCCESS('Alunos e Livros populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando Empréstimos...'))
     

        for _ in range(15):
            data_emprestimo = fake.date_between(start_date='-30d', end_date='today')
            Emprestimos.objects.create(
                aluno=random.choice(alunos),
                livro=random.choice(livros),
                data_emprestimo=data_emprestimo,
                data_devolucao=fake.date_between(start_date=data_emprestimo, end_date='+30d')
            )
        self.stdout.write(self.style.SUCCESS('Empréstimos populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando Médicos e Pacientes...'))
        medicos = [
            Medico.objects.create(
                nome=fake.name(),
                crm=str(fake.random_number(digits=6)),
                especialidade=fake.job()
            ) for _ in range(5)
        ]
        pacientes = [
            Paciente.objects.create(
                nome=fake.name(),
                telefone=fake.phone_number(),
                data_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=80)
            ) for _ in range(10)
        ]
        self.stdout.write(self.style.SUCCESS('Médicos e Pacientes populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando Consultas...'))
        for _ in range(15):
            Consulta.objects.create(
            medico=random.choice(medicos),
            paciente=random.choice(pacientes),
            data_consulta=timezone.make_aware(fake.date_time_this_month()),  
            descricao=fake.text()
            )
        self.stdout.write(self.style.SUCCESS('Consultas populadas com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Populando Professores, Turmas e Alunos...'))
        professores = [
            Professor.objects.create(
                nome=fake.name(),
                email=fake.email(),
                disciplina=fake.word()
            ) for _ in range(5)
        ]
        turmas = [
            Turma.objects.create(
                nome=fake.word(),
                professor=random.choice(professores),
                horario=f"{random.randint(7, 22)}:00"
            ) for _ in range(5)
        ]
        for _ in range(20):
            AlunoTurma.objects.create(
                nome=fake.name(),
                curso=fake.word(),
                matricula=fake.unique.random_number(digits=6),
                turma=random.choice(turmas)
            )
        self.stdout.write(self.style.SUCCESS('Professores, Turmas e Alunos populados com sucesso! ✅'))

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
