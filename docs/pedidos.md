## API Endpoints

### Pedidos

- Lista/Criar: `/api/pedidos/`
- Detalhes/Atualizar/Deletar: `/api/pedidos/{id}/`

### Clientes

- Lista/Criar: `/api/clientes/`
- Detalhes/Atualizar/Deletar: `/api/clientes/{id}/`

### Itens do Pedido

- Lista/Criar: `/api/itenspedido/`
- Detalhes/Atualizar/Deletar: `/api/itenspedido/{id}/`

## Exemplos de Uso

### Criando um Pedido

```json
POST /api/pedidos/
{
    "cliente": null,
    "total": null,
    "itens": [
        {
        "produto": "",
        "quantidade": null,
        "preco": null
        },
    ]
}
```

### Criando um Cliente

```json
POST /api/clientes/
{
    "nome": "",
    "email": "",
    "telefone": ""
}
```

### Criando um Item do Pedido

```json
POST /api/itenspedido/
{
    "pedidos": null,
    "produto": "",
    "quantidade": null,
    "preco": null
}
```
