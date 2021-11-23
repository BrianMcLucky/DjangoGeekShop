import json
import os.path

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)


# Create your views here.

def index(request):
    content = {
        'title': 'Geekshop',
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')

    content = {
        'title': 'Geekshop - Каталог', }
    content['products'] = json.load(open(file_path, encoding='utf-8'))


    return render(request, 'mainapp/products.html', content)
