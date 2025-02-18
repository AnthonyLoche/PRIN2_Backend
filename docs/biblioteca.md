## API Endpoints

### Livros

- Lista/Criar: `/api/livros/`
- Detalhes/Atualizar/Deletar: `/api/livros/{id}/`

### Alunos

- Lista/Criar: `/api/alunos/`
- Detalhes/Atualizar/Deletar: `/api/alunos/{id}/`

### Empréstimos

- Lista/Criar: `/api/emprestimos/`
- Detalhes/Atualizar/Deletar: `/api/emprestimos/{id}/`

## Exemplos de Uso

### Criando um Livro

```json
POST /api/livros/
{
    "titulo": "",
    "autor": "",
    "ano_publicacao": null
}
```

### Criando um Aluno

```json
POST /api/alunos/
{
    "nome": "",
    "matricula": "",
    "curso": ""
}
```

### Criando um Empréstimo

```json
POST /api/emprestimos/
{
    "aluno": null,
    "livro": null,
    "data_devolucao": null
}
```