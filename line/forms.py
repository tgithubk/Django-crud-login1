from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment', max_length=100)
    
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(), min_length=8)

class SignupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(),label="password")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','password')
        # フィールド名指定
        labels = {'username':"username",'password':"password"}
