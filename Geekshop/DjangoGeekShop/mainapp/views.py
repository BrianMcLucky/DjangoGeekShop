from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    content = {
        'title': 'Geekshop',
    }
    return render(request, 'index.html', content)


def products(request):

    content = {
        'title': 'Geekshop - Каталог',
    }
    return render(request, 'products.html', content)
