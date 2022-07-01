from django.contrib import admin
from .models import Category, Quiz, Question, Answer
from nested_admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline


class AnswerInline(NestedTabularInline):
    model = Answer
    extra = 4


class QuestionInline(NestedTabularInline):
    model = Question
    extra = 1
    inlines = [AnswerInline]

class QuizAdmin(NestedModelAdmin):
    inlines = [QuestionInline]
    
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)

admin.site.register(Question)
admin.site.register(Answer)


