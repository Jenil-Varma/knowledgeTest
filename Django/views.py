from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def error(request):
    return render(request, 'error.html')