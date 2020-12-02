from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/lojas/', views.LojaList.as_view()),
    path('api/produtos/', views.ProdutoList.as_view()),
    path('api/promocoes/', views.PromocaoList.as_view()),
    path('api/lojas/<int:pk>/', views.LojaDetail.as_view()),
    path('api/produtos/<int:pk>/', views.ProdutoDetail.as_view()),
    path('api/promocoes/<int:pk>/', views.PromocaoDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)