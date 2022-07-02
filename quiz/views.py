from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Quiz, Question, Answer
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from .permissions import StafCUDAuthenticatedOnlyRead

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)

class CategoryGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)
    lookup_field = "id"


class QuizListCreateView(ListCreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)

    def get_queryset(self):
        category_name = self.kwargs['category']
        return Quiz.objects.filter(category__name__iexact = category_name)

class QuizGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)
    lookup_field = "id"


class QuestionListCreateView(ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)

    def get_queryset(self):
        quiz_title = self.kwargs['title']
        return Question.objects.filter(quiz__title__iexact=quiz_title)

class QuestionGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)
    lookup_field = "id"


class AnswerGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (StafCUDAuthenticatedOnlyRead,)
    lookup_field = "id"




