from django.urls import path
from .views import (
    home,
    sign_in,
    log_out,
    course,
    profile,
    aboutus,
    payment_finish,
)

urlpatterns = [
    path("", home, name="home"),
    path("payment_finish", payment_finish, name="payment_finish"),
    path("profile", profile, name="profile"),
    path("aboutus", aboutus, name="aboutus"),
    path("course", course, name="course"),
    path("sign-in", sign_in, name="sign-in"),
    path("log-out", log_out, name="log-out"),
]
