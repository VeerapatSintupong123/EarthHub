from .forms import RegisterForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, "home.html")


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "sign-up.html", {"form": form})
