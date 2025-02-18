from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.telefone}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} - {self.data} - {self.total}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    produto = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.pedido} - {self.produto} - {self.quantidade} - {self.preco}"
    
    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"