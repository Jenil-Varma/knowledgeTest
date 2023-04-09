from django.contrib import admin

from .models import User


class UserDetail(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'hide_password')


admin.site.register(User, UserDetail)

