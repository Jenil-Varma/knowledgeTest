from django.shortcuts import render, redirect


def home(request):
    return redirect('quiz:index')
    #return render(request, 'base.html')


def error(request):
    return render(request, 'error.html')