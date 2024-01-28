from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


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
    else:
        if request.user.is_authenticated:
            return redirect("profile")
    return render(request, "sign-in.html")


def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course")
    else:
        form = RegisterForm()

    return render(request, "home.html", {"form": form})


def course(request):
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": "price_1OdQvaI73qQoyJE7yPV0Uj0M",
                        "quantity": 1,
                    },
                ],
                mode="payment",
                success_url=request.build_absolute_uri("profile"),
                cancel_url=request.build_absolute_uri("course"),
            )

            return redirect(checkout_session.url)
        except Exception:
            return redirect("home")

    return render(request, "course.html")


def profile(request):
    if not request.user.is_authenticated:
        return redirect("home")
    return render(request, "profile.html")


def aboutus(request):
    return render(request, "aboutus.html")
