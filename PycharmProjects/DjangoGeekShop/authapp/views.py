from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect

# Create your views here.
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    content = {
        'title': 'Geekshop | Login',
        'form': form
    }
    return render(request, 'authapp/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration success')
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    content = {
        'title': 'Geekshop | Registration',
        'form': form
    }
    return render(request, 'authapp/register.html', content)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile change success')


        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)

    total_quantity = 0
    total_sum = 0
    baskets = Basket.objects.filter(user=request.user)
    for basket in baskets:
        total_sum = basket.sum()
        total_quantity += basket.quantity

    content = {
        'title': 'Geekshop | Profile',
        'form': UserProfileForm(instance=request.user),
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity,

    }
    return render(request, 'authapp/profile.html', content)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
