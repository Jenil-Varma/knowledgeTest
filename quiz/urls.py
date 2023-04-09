from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('quiz-homepage/', views.quiz_homepage, name='quiz-homepage'),

]
