from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django import forms
from authapp.models import User
from authapp.validator import validate_name


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(), validators=[validate_name])

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter user name'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    #
    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     if not data.isalpha():
    #         raise ValidationError('User name cannot contain numbers.')
    #     return data


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter user name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password again'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)
    first_name = forms.CharField(widget=forms.TextInput(), validators=[validate_name])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


    def clean_image(self):
        img = self.cleaned_data['image']
        file_size = self.file.size

        if not img:
            raise ValidationError('No image.')

        else:
            if file_size > 1*1024*1024:
                raise ValidationError('File too large, max size 1 mb.')

        return img










