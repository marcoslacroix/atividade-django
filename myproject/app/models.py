from django.db import models
from django.utils import timezone

class Produto(models.Model):

    CATEGORIAS = [
    ('hamburguer de carne', 'Hambúrguer de Carne'),
    ('hamburguer de frango', 'Hambúrguer de Frango'),
    ('acompanhamento', 'Acompanhamento'),
    ('sobremesa', 'Sobremesa'),
    ('vegetariano', 'Vegetariano'),
    ]

    nome_produto = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/image",blank=True)
    descricao = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='hamburguer de carne')


    class Meta:
        verbose_name = ("Produto")
        verbose_name_plural = ("Produtos")

    def __str__(self):
        return self.nome_produto

class Loja(models.Model):
    nome = models.CharField(max_length=100)    
    cidade = models.CharField(max_length=100)  
    uf = models.CharField(max_length=2) 
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Loja")
        verbose_name_plural = ("Lojas")

    def __str__(self):
        return self.nome

class Promocao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    preco = models.IntegerField()
    cupom = models.CharField(max_length=100, blank=True)
    destaque = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Promoção")
        verbose_name_plural = ("Promoções")
        ordering = ('destaque',)

