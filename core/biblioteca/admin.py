from django.contrib import admin

from .models import Aluno, Livros, Emprestimos

admin.site.register(Aluno)
admin.site.register(Livros)
admin.site.register(Emprestimos)