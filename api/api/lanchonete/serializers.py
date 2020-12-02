from .models import Loja, Produto, Promocao
from rest_framework import serializers

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id', 'nome', 'cidade', 'uf', 'email']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome_produto', 'image', 'descricao', 'categoria']

class PromocaoSerializer(serializers.ModelSerializer):
    produto = serializers.SlugRelatedField(many=False, read_only=False, queryset=Produto.objects.all(),slug_field='id') 
    loja = serializers.SlugRelatedField(many=False, read_only=False, queryset=Loja.objects.all(),slug_field='id') 
    class Meta:
        model = Promocao
        fields = ['id', 'preco', 'cupom', 'destaque', 'loja', 'produto']