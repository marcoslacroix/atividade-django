from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #importação dos métodos utilizados para ver o login/logout e autenticação
from .models import Promocao, Loja, Produto
from .serializers import LojaSerializer, ProdutoSerializer, PromocaoSerializer
from django.http import Http404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #método para verificar se a senha está correta
        if user is not None:
            login(request, user)
            return redirect("/") # redireciona para a página principal
        else:
            return redirect('/login?erro=true')
    else:
        mensagem_erro = 'Usuário e/ou senha não conferem.' if 'erro' in request.GET else ''
    return render(request, 'login.html', {'mensagem_erro': mensagem_erro})

def do_logout(request):
    logout(request)
    return redirect('/login') #redireciona para a página de login novamente

def do_search_promocao(request):

    promocoes = Promocao.objects.order_by('-destaque')

    return render(request, "index.html", {"promocoes": promocoes})

class LojaList(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        lojas = Loja.objects.all()
        if 'nome' in get_data:
            lojas = lojas.filter(nome=get_data.get('nome'))   
        serializer = LojaSerializer(lojas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LojaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LojaDetail(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Loja.objects.get(pk=pk)
        except Loja.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loja = self.get_object(pk)
        serializer = LojaSerializer(loja)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        loja = self.get_object(pk)
        serializer = LojaSerializer(loja, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        loja = self.get_object(pk)
        serializer = LojaSerializer(loja, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loja = self.get_object(pk)
        loja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProdutoList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        produtos = Produto.objects.all()
        if 'categoria' in get_data:
            produtos = produtos.filter(categoria=get_data.get('categoria'))  
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdutoDetail(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        produto = self.get_object(pk)
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        produto = self.get_object(pk)
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PromocaoList(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        get_data = request.query_params
        promocoes = Promocao.objects.all()
        if 'preco' in get_data:
            promocoes = promocoes.filter(preco=get_data.get('preco'))
        elif 'favoritar' in get_data:
            promocoes = promocoes.filter(favoritar=get_data.get('favoritar'))  
        serializer = PromocaoSerializer(promocoes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PromocaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PromocaoDetail(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Promocao.objects.get(pk=pk)
        except Promocao.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        promocao = self.get_object(pk)
        serializer = PromocaoSerializer(promocao)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        promocao = self.get_object(pk)
        serializer = PromocaoSerializer(promocao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        promocao = self.get_object(pk)
        serializer = PromocaoSerializer(promocao, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        promocao = self.get_object(pk)
        promocao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



