from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from .permissions import StafCUDAuthenticatedOnlyRead

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)

class QuizListView(ListCreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)

    def get_queryset(self):
        category_name = self.kwargs['category']
        return Quiz.objects.filter(category__name__iexact = category_name)

class QuestionListView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)

    def get_queryset(self):
        quiz_title = self.kwargs['title']
        return Question.objects.filter(quiz__title__iexact=quiz_title)


