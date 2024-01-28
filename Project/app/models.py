from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    buyGeology = models.CharField(max_length=255, default="NO")
    buyGeography = models.CharField(max_length=255, default="NO")

    def __str__(self):
        return f"{self.user.email} {self.buyGeography} {self.buyGeology}"
