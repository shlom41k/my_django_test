from django.contrib import admin
from .models import Questions, Answer, Result


# Register your models here.
@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["question", "answer", "theme"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer", "question"]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ["date", "user", "total_questions", "correct_answers", "result"]
