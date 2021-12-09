from django.urls import path

from admins.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryAdminView, \
    CategoryCreateAdminView, CategoryUpdateAdminView, CategoryDeleteAdminView, ProductAdminView, ProductCreateAdminView, \
    ProductUpdateAdminView, ProductDeleteAdminView, IndexTemplateView

app_name = 'admins'
urlpatterns = [

    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('category/', CategoryAdminView.as_view(), name='admin_category'),
    path('category-create/', CategoryCreateAdminView.as_view(), name='admin_category_create'),
    path('category-update/<int:pk>', CategoryUpdateAdminView.as_view(), name='admin_category_update'),
    path('category-delete/<int:pk>', CategoryDeleteAdminView.as_view(), name='admin_category_delete'),
    path('product/', ProductAdminView.as_view(), name='admin_product'),
    path('product-create/', ProductCreateAdminView.as_view(), name='admin_product_create'),
    path('product-update/<int:pk>', ProductUpdateAdminView.as_view(), name='admin_product_update'),
    path('product-delete/<int:pk>', ProductDeleteAdminView.as_view(), name='admin_product_delete'),

]
