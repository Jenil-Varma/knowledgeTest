from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import User


def index(request):
    return render(request, 'quiz/index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.authenticate(username, password)
        if user is not None:
            return redirect('quiz-homepage')
        else:
            print('Here2')
            return render(request, 'index.html', {'error_message': 'Invalid login'})
    else:
        return redirect(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(full_name=full_name, username=username, password=password)
        return redirect(reverse('quiz-homepage'))
    return render(request, 'quiz/registration.html')

def quiz_homepage(request):
    return render(request, 'quiz/quiz-homepage.html')
