from django.contrib import admin

from respondent.models import Answer, Question


# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at")
    search_fields = ("text",)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question_id", "user_id", "created_at","text")
    search_fields = ("text", "user_id")