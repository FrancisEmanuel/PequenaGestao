from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)


    def __str__(self):
        return self.nome_produto

# Create your models here.


