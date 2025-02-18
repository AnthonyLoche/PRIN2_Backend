from django.shortcuts import render


from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Pedidos, ItensPedido, Clientes
from .serializers import PedidosListSerializer, ItensPedidoListSerializer, ClientesSerializer, PedidosCreateSerializer, ItensPedidoCreateSerializer
from rest_framework.decorators import api_view

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PedidosListSerializer
        return PedidosCreateSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer_data = {
                'cliente': serializer.validated_data.pop('cliente'),
                'total': serializer.validated_data.pop('total')
            }

            pedido_output = Pedidos.objects.create(**serializer_data)
            
            itens = serializer.validated_data.pop('itens')

            for item in itens:
                ItensPedido.objects.create( 
                    pedido=pedido_output,
                    produto=item['produto'],
                    quantidade=item['quantidade'],
                    preco=item['preco']
            )
            
            return Response({'message': 'Pedido criado com sucesso!'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItensPedido.objects.all()
    serializer_class = ItensPedidoListSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer