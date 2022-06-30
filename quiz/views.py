from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Category, Quiz, Question, Answer
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer


class CategoryListView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizListView(ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        category_name = self.kwargs['category']
        cat_id = Category.objects.get(name=category_name).id
        return Quiz.objects.filter(category_id = cat_id)

class QuestionListView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_title = self.kwargs['title']
        quiz_id = Quiz.objects.get(title=quiz_title).id
        return Question.objects.filter(quiz_id=quiz_id)


