from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ["email", "phone_number", "username"]
    list_display = ["pk", "email", "phone_number", "username"]
