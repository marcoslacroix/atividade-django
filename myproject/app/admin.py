from django.contrib import admin
from .models import Loja, Produto, Promocao

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_produto",)

class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "uf", "email")

class CategoriaProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria",)

class PromocaoAdmin(admin.ModelAdmin):
    list_display = ("produto",)

admin.site.register(Loja, LojaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Promocao, PromocaoAdmin)