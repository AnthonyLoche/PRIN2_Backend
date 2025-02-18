# core/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pedidos': request.build_absolute_uri(reverse('pedidos-list')),  # Use 'pedidos-list'
        'clientes': request.build_absolute_uri(reverse('clientes-list')),  # Use 'clientes-list'
        'produtos': request.build_absolute_uri(reverse('produtos-list')),  # Use 'produtos-list'
        'estoque': request.build_absolute_uri(reverse('estoque-list')),  # Use 'estoque-list'
    })
