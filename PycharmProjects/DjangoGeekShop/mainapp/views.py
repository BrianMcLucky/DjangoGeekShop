import os.path

from django.shortcuts import render
from mainapp.models import Product, ProductCategory

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    content = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'Geekshop - Каталог',
    }
    content['products'] = Product.objects.all()
    content['categories'] = ProductCategory.objects.all()

    return render(request, 'mainapp/products.html', content)
