from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://fakestoreapi.com/products')
    produtos = []
    if response.status_code == 200:
        products = response.json()
        for product in products:
            prod = {
                'id':product['id'],
                'title': product['title'],
                'image': product['image'],
                'price': product['price'],
                'category': product['category'],
                'description': product['description'],
            }
            produtos.append(prod)
    else:
        print(f"Erro: {response.status_code}")

    if request.method == 'POST':
        categoria = request.POST.get('busca')
        response = requests.get(f'https://fakestoreapi.com/products/category/{categoria}')
        if response.status_code == 200:
            produtos = []
            products = response.json()
            for product in products:
                prod = {
                    'id':product['id'],
                    'title': product['title'],
                    'image': product['image'],
                    'price': product['price'],
                    'category': product['category'],
                    'description': product['description'],
                }
                produtos.append(prod)
        else:
            print(f"Erro: {response.status_code}")

    return render(request, 'index.html', {"produto": produtos})

def PageCompra(request,id):
    response = requests.get('https://fakestoreapi.com/products')
    produtos = []
    if response.status_code == 200:
        products = response.json()
        for product in products:
            if product['id'] == id:
                prod = {
                    'title': product['title'],
                    'image': product['image'],
                    'price': product['price'],
                    'category': product['category'],
                    'description': product['description'],
                }
                produtos.append(prod)
                break
    else:
        print(f"Erro: {response.status_code}")
    
    return render(request,'compra.html',{"produto":produtos})
