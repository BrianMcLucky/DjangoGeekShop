from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryFormAdmin, ProductFormAdmin
from authapp.models import User
from mainapp.mixin import CustomDispatchMixin, BaseClassContextMixin
from mainapp.models import ProductCategory, Product


class IndexTemplateView(TemplateView):
    template_name = 'admins/admin.html'


class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Admin | Users'


class UserCreateView(CreateView, CustomDispatchMixin, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Admin | Users create'


class UserUpdateView(UpdateView, CustomDispatchMixin, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Admin | Users refactor'


class UserDeleteView(DeleteView, CustomDispatchMixin, BaseClassContextMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Admin | Users delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryAdminView(ListView, CustomDispatchMixin, BaseClassContextMixin):
    template_name = 'admins/admin-category-read.html'
    model = ProductCategory
    title = 'Admin | Category list'

    def get_queryset(self):
        if self.kwargs:
            return ProductCategory.objects.filter(id=self.kwargs.get('pk'))
        else:
            return ProductCategory.objects.all()


class CategoryCreateAdminView(CreateView, CustomDispatchMixin, BaseClassContextMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    form_class = CategoryFormAdmin
    success_url = reverse_lazy('admins:admin_category')
    title = 'Admin | Category create'


class CategoryUpdateAdminView(UpdateView, CustomDispatchMixin, BaseClassContextMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryFormAdmin
    success_url = reverse_lazy('admins:admin_category')
    title = 'Admin | Category refactor'


class CategoryDeleteAdminView(DeleteView, CustomDispatchMixin, BaseClassContextMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryFormAdmin
    success_url = reverse_lazy('admins:admin_category')
    title = 'Admin | Category delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductAdminView(ListView, CustomDispatchMixin, BaseClassContextMixin):
    template_name = 'admins/admin-product-read.html'
    model = Product
    title = 'Admin | Product list'


class ProductCreateAdminView(CreateView, CustomDispatchMixin, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    form_class = ProductFormAdmin
    success_url = reverse_lazy('admins:admin_product')
    title = 'Admin | Product create'


class ProductUpdateAdminView(UpdateView, CustomDispatchMixin, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductFormAdmin
    success_url = reverse_lazy('admins:admin_product')
    title = 'Admin | Product refactor'


class ProductDeleteAdminView(DeleteView, CustomDispatchMixin, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductFormAdmin
    success_url = reverse_lazy('admins:admin_product')
    title = 'Admin | Product delete'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
