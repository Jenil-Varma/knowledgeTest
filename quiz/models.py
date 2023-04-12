import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    last_login = models.DateTimeField(null=True, blank=True)

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

class QuizTopic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Question(models.Model):
    topic = models.ForeignKey(QuizTopic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_topic = models.ForeignKey(QuizTopic, on_delete=models.CASCADE)
    marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.quiz_topic} - {self.marks}"
