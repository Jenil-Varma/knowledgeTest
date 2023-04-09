import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    def hide_password(self):
        return '*' * len(self.password)

    hide_password.short_description = 'Password'

    def authenticate(self, password):
        try:
            user = User.objects.get(username=self)
        except User.DoesNotExist:
            return None
        if user.password == password:
            return user
        return None
