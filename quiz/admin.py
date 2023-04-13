from django.contrib import admin
from .models import Topic, Question, Choice, Quiz, QuizQuestion

# Register your models here.

# quiz_date in the Quiz table has an auto_now_add attribute. This field is not going to display on the admin page. So add this to show as read-only.
class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('quiz_date',)


admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizQuestion)

