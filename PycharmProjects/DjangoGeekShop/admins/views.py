from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryFormAdmin, ProductFormAdmin
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Admin | Registration',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):
    user_select = User.objects.get(pk=pk)

    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'GeekShop - Admin | Update',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryFormAdmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryFormAdmin()
    context = {
        'title': 'Admin | Category creation',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryFormAdmin(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategoryFormAdmin(instance=category_select)
    context = {
        'title': 'GeekShop - Admin | Update',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, pk):
    if request.method == 'POST':
        category = ProductCategory.objects.get(pk=pk)
        category.is_active = False
        category.save()

    return HttpResponseRedirect(reverse('admin:admin_category'))


@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductFormAdmin(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
    else:
        form = ProductFormAdmin()
    context = {
        'title': 'Admin | Product creation',
        'form': form
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, pk):
    product_select = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductFormAdmin(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
    else:
        form = ProductFormAdmin(instance=product_select)
    context = {
        'title': 'GeekShop - Admin | Update',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'admins/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.is_active = False
        product.save()

    return HttpResponseRedirect(reverse('admin:admin_product'))

