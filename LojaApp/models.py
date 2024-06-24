from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    dataPub = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to = 'img_produto/',null = True,blank = True,max_length=500)
    def __str__(self):
        return self.nome
    

class Vendas(models.Model):
    produto = models.ForeignKey(Produtos,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valorTotal = models.FloatField()

    def __str__(self):
        return self.produto.nome