from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user_email",
        "buyGeography",
        "buyGeology",
    )

    def user_email(self, obj):
        return obj.user.email


admin.site.register(UserProfile, UserProfileAdmin)
