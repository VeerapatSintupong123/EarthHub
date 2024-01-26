from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    response = redirect("sign-up")
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
            return redirect("course")
    else:
        if request.user.is_authenticated:
            return redirect("course")
    return render(request, "sign-in.html")


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course")
    else:
        form = RegisterForm()
    return render(request, "sign-up.html", {"form": form, "username": None})


def course(request):
    if not request.user.is_authenticated:
        return redirect("sign-up")
    return render(request, "course.html")
