from django import forms

from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(),required=False)


    class Meta():
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name','age', 'password1', 'password2')



    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)


        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfilerForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())


    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryFormAdmin(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    description = forms.CharField(widget=forms.TextInput(), required=False)



    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryFormAdmin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ProductFormAdmin(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    # image = forms.ImageField(upload_to='product_image', blank=True)
    description = forms.CharField(widget=forms.TextInput(), required=False)
    price = forms.DecimalField(widget=forms.DecimalField)
    quantity = forms.IntegerField(widget=forms.IntegerField())
    # category = forms.ModelChoiceField(ProductCategory)

    class Meta():
        model = Product
        fields = ('name', 'description', 'price','quantity', 'category')



    def __init__(self, *args, **kwargs):
        super(ProductFormAdmin, self).__init__(*args, **kwargs)


        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
