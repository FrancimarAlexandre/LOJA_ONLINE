from django.shortcuts import render

# Create your views here.
import requests




def index(request):
    response = requests.get('https://fakestoreapi.com/products')
    produtos = []
    if response.status_code == 200:
        products = response.json()
        for product in products:
            prod ={
                'title':product['title'],
                'image':product['image'],
                'price':product['price'],
                'category':product['category'],
                'description':product['description'],
            }
            produtos.append(prod)
            
    else:
        print(f"Erro: {response.status_code}")
    
    return render(request,'index.html',{"produto":produtos})