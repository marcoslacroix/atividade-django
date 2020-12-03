"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import do_login, do_logout, do_search_promocao, ProdutoList, LojaList, PromocaoList, LojaDetail, ProdutoDetail, PromocaoDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', do_search_promocao),
    path('login/', do_login),
    path('logout/', do_logout),
    path('produtos/', ProdutoList.as_view()),
    path('lojas/', LojaList.as_view()),
    path('promocoes/', PromocaoList.as_view()),
    path('lojas/<int:pk>/', LojaDetail.as_view()),
    path('produtos/<int:pk>/', ProdutoDetail.as_view()),
    path('promocoes/<int:pk>/', PromocaoDetail.as_view())


]
