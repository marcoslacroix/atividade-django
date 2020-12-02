# Generated by Django 3.1.2 on 2020-12-01 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Loja',
                'verbose_name_plural': 'Lojas',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='media/image')),
                ('descricao', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('hamburguer de carne', 'Hambúrguer de Carne'), ('hamburguer de frango', 'Hambúrguer de Frango'), ('acompanhamento', 'Acompanhamento'), ('sobremesa', 'Sobremesa'), ('vegetariano', 'Vegetariano')], default='hamburguer de carne', max_length=50)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.IntegerField()),
                ('cupom', models.CharField(blank=True, max_length=100)),
                ('destaque', models.BooleanField()),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.loja')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
            ],
            options={
                'verbose_name': 'Promoção',
                'verbose_name_plural': 'Promoções',
            },
        ),
    ]
