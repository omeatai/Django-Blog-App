from django import forms
from django.utils.html import format_html
from django.contrib.auth.models import User
from .models import Article

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        initial='',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label='Password',
        required=True,
        max_length=50,
        help_text=format_html('<span class="red">50 characters max.</span>'),
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        else:
            return cd['password2']

class ArticleRegistrationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'description')