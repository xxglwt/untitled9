# author
# -*- coding:utf-8 -*-
# create time 2020年02月19日 20:45
from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=4, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': '', 'placeholder': 'username'}))
    password = forms.CharField(label='密码', max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "password"}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (('male', '男'), ('female', '女'))
    username = forms.CharField(max_length=4, label='用户名', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=10,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))
    password2 = forms.CharField(label="确认密码", max_length=10,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))
    email = forms.EmailField(label="电子邮箱", max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="性别", choices=gender)
    captcha = CaptchaField(label="验证码")
   