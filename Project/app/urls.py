from django.urls import path
from .views import sign_up, sign_in, log_out, course

urlpatterns = [
    path("", sign_up, name="sign-up"),
    path("course", course, name="course"),
    path("sign-in", sign_in, name="sign-in"),
    path("log-out", log_out, name="log-out"),
]
