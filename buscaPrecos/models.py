from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    preco = models.FloatField()
    foto = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Produtos'

    def __str__(self):
        return self.nome