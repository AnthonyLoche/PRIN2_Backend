## API Endpoints

### Pacientes

- Lista/Criar: `/api/pacientes/`
- Detalhes/Atualizar/Deletar: `/api/pacientes/{id}/`

### Médicos

- Lista/Criar: `/api/medicos/`
- Detalhes/Atualizar/Deletar: `/api/medicos/{id}/`

### Consultas

- Lista/Criar: `/api/consultas/`
- Detalhes/Atualizar/Deletar: `/api/consultas/{id}/`

## Exemplos de Uso

### Criando um Paciente

```json
POST /api/pacientes/
{
    "nome": "",
    "data_nascimento": null,
    "telefone": ""
}
```

### Criando um Médico

```json
POST /api/medicos/
{
    "nome": "",
    "especialidade": "",
    "crm": ""
}
```

### Criando uma Consulta

```json
POST /api/consultas/
{
    "paciente": null,
    "medico": null,
    "data_consulta": null,
    "descricao": ""
}
```
