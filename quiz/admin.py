from django.contrib import admin
from .models import Topic, Question, Choice, Quiz

# Register your models here.

admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Quiz)
