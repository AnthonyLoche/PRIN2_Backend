from django.contrib import admin
from .models import Pedidos,   ItensPedido, Clientes

admin.site.register(Pedidos)
admin.site.register(ItensPedido)
admin.site.register(Clientes)