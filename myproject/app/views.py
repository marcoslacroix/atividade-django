from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #importação dos métodos utilizados para ver o login/logout e autenticação

from .models import Promocao, Loja

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

def filtro(request):

    lojas = Loja.objects.all()
    promocoes = Promocao.objects.all()
    produtos = Produto.objects.all()


    return render(request, "index.html", {})
