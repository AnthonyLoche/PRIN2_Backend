from rest_framework import serializers
from .models import Pedidos, Clientes, ItensPedido

class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = '__all__'

class ItensPedidoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItensPedido
        fields = [
            'pedido', 
            'produto', 
            'quantidade', 
            'preco'
        ]

class ItensPedidoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItensPedido
        fields = [
            'produto', 
            'quantidade', 
            'preco'
        ]

class PedidosListSerializer(serializers.ModelSerializer):
    itens = serializers.SerializerMethodField()
    cliente = ClientesSerializer()
    
    class Meta:
        model = Pedidos
        fields = [
            'cliente', 
            'data', 
            'total', 
            'itens'
        ]

    def get_itens(self, obj):
        itens = ItensPedido.objects.filter(pedido=obj)
        return ItensPedidoListSerializer(itens, many=True).data

class PedidosCreateSerializer(serializers.ModelSerializer):
    itens = ItensPedidoCreateSerializer(many=True, write_only=True)
    
    class Meta:
        model = Pedidos
        fields = [
            'cliente', 
            'data', 
            'total', 
            'itens'
        ]
