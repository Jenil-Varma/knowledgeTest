from django.urls import path

from . import views

app_name = "quiz"
urlpatterns = [
    path('', views.index, name='index'),
    path('select_topic/', views.select_topic, name='select_topic'),
    path('take_quiz/', views.take_quiz, name='take_quiz'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('quiz_result/<int:quiz_id>/', views.quiz_results, name='quiz_result'),
]
