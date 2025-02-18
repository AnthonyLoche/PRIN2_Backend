## API Endpoints

### Professores

- Lista/Criar: `/api/professores/`
- Detalhes/Atualizar/Deletar: `/api/professores/{id}/`

### Turmas

- Lista/Criar: `/api/turmas/`
- Detalhes/Atualizar/Deletar: `/api/turmas/{id}/`

### Alunos-Turmas

- Lista/Criar: `/api/alunos-turmas/`
- Detalhes/Atualizar/Deletar: `/api/alunos-turmas/{id}/`

## Exemplos de Uso

### Criando um Professor

```json
POST /api/professores/
{
    "nome": "",
    "disciplina": "",
    "email": ""
}
```

### Criando uma Turma

```json
POST /api/turmas/
{
    "nome": "",
    "professor": null,
    "horario": ""
}
```

### Criando um Aluno-Turma

```json
POST /api/alunos-turmas/
{
    "nome": "",
    "matricula": "",
    "curso": "",
    "turma": null
}
```