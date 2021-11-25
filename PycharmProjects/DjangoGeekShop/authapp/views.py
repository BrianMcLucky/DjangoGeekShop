from django.shortcuts import render

# Create your views here.

def login(request):
    content = {
        'title': 'Geekshop | Login',
    }
    return render(request, 'authapp/login.html', content)



def register(request):
    content = {
        'title': 'Geekshop | Registration',
    }
    return render(request, 'authapp/register.html', content)