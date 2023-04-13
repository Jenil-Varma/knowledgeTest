from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    correct_option = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    quiz_date = models.DateTimeField("Quiz date", auto_now_add=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.score)


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.question)