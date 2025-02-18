import subprocess
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Executa os comandos makemigrations e migrate para diferentes apps'

    def handle(self, *args, **kwargs):
        apps = ['consultas', 'pedidos', 'turmas', 'biblioteca']

        for app in apps:
            self.stdout.write(f'Executando makemigrations para {app}...')
            subprocess.run(['pdm', 'makemigrations', app], check=True)
            
            self.stdout.write(f'Executando migrate para {app}...')
            subprocess.run(['pdm', 'migrate', app], check=True)
        
        subprocess.run(['pdm', 'migrate'], check=True)

        self.stdout.write(self.style.SUCCESS('Comandos executados com sucesso para todos os apps!'))
