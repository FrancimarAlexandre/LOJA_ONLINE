from django.shortcuts import render
from .models import Produtos,Vendas
# Create your views here.

def index(request):
    produtos = Produtos.objects.all()
    
    return render(request,'index.html',{"produto":produtos})