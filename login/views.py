from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
import hashlib


# Create your views here.
def hash_code(s, salt='wangtie'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    request.session.user_name = "王铁"

    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = "用户名不能为空"
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            password=hash_code(password)
            # username = request.POST.get("username")
            # password = request.POST.get("password")
            # if username.strip() and password:

            try:
                user = models.User.objects.get(name=username)
            except:
                message = "用户不存在"
                return render(request, 'login/login.html', locals())
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                print(username, password)
                return redirect('/index/')
            else:
                message = "密码错误"
                return render(request, 'login/login.html', locals())
        else:
            # message = "用户或者密码不能为空"
            # message=forms.UserForm().errors
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容"
        if register_form.is_valid():
            username = register_form.cleaned_data.get("username")
            password = register_form.cleaned_data.get("password")
            password2 = register_form.cleaned_data.get("password2")
            email = register_form.cleaned_data.get("email")
            sex = register_form.cleaned_data.get("sex")

            if password != password2:
                message = "两次输入的密码不一致"
                return render(request, "login/register.html", locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "用户名已经存在"
                    return render(request, 'login/register.html', locals())
                same_email = models.User.objects.filter(email=email)
                if same_email:
                    message = "注册邮件已经存在"
                    return render(request, 'login/register.html', locals())
                newUser = models.User()
                newUser.name = username
                newUser.password =hash_code(password)
                newUser.email = email
                newUser.sex = sex
                newUser.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')
