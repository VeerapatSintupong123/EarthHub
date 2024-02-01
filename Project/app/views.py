from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm
from .models import UserProfile
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    elif request.user.is_authenticated:
        return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "sign-in.html", {"form": form})


def home(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)
            profile.save()
            return redirect("course")
    else:
        form = RegisterForm()
    return render(request, "home.html", {"form": form})


@login_required(login_url="sign-in")
def course(request):
    list_items = [
        {
            "price": "price_1OdQvaI73qQoyJE7yPV0Uj0M",
            "quantity": 1,
        },
        {
            "price": "price_1Oeh4bI73qQoyJE7Tfkr9nC9",
            "quantity": 1,
        },
    ]

    if request.method == "POST":
        try:
            selected_id = int(request.POST.get("selected_course", -1))
            if 0 <= selected_id < len(list_items):
                request.session["selected_id"] = selected_id

                checkout_session = stripe.checkout.Session.create(
                    payment_method_types=["card"],
                    line_items=[list_items[selected_id]],
                    mode="payment",
                    success_url=request.build_absolute_uri("payment_finish"),
                    cancel_url=request.build_absolute_uri("course"),
                )

                return redirect(checkout_session.url)
        except Exception as e:
            print(e)
            return redirect("home")
    return render(request, "course.html")


@login_required(login_url="sign-in")
def payment_finish(request):
    current_user = request.user
    print(current_user)
    user_profile = UserProfile.objects.get(user=current_user)
    selected_id = request.session.get("selected_id", -1)

    if selected_id == 0:
        user_profile.buyGeography = "YES"
        print("update buyGeography")
    elif selected_id == 1:
        user_profile.buyGeology = "YES"
        print("update buyGeology")

    user_profile.save()

    request.session.pop("selected_id", None)

    return redirect("course")


@login_required(login_url="sign-in")
def profile(request):
    return render(request, "profile.html")


def aboutus(request):
    return render(request, "aboutus.html")
