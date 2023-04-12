from django.contrib import admin

from .models import User, Question, Choice, QuizResult


class UserDetail(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'hide_password')


admin.site.register(User, UserDetail)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(QuizResult)

