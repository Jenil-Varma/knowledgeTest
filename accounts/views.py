from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from accounts.models import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'
