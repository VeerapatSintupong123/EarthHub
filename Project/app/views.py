from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "home.html", {"username": username})


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    response = redirect("home")
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "sign-in.html")


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "sign-up.html", {"form": form, "username": None})
