# redirect login olan useri yonlendirmek ucun her hansisa sehifeye
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User  # user qeydiyyat
# user login #authenticate i yoxlamaq ucun
from django.contrib.auth import login, authenticate, logout

# # Create your views here.


def account(request):
    return render(request, "account.html")


def register(request): # ya post metodunu almali ya da bos gondermeli

    if request.user.is_authenticated:  # Kullanıcı zaten oturum açmışsa
        return redirect("home")  # Home sayfasına yönlendir


    form = RegisterForm(request.POST or None)

    if form.is_valid():  # eger kodda her sey dogrudursa username ve passwordun deyerlerini al
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()  # new user ucun aldigin deyerleri databazaya daxil etmek

        login(request, newUser)  # qeydiyyatdan kecen user avtomatik login olsun

        return redirect("home")  # qeyd kecen sexs home_page e yonlendirilir

    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form,
    }

    if form.is_valid():  # eger kodda her sey dogrudursa username ve passwordun deyerlerini al
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:  # eger bos daxil edilmisse yeniden login sehifesine kecid
            return render(request, "login.html")

        login(request, user)
        return redirect("home")

    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("home")
