from django.urls import path, include
from .views import CategoryListView, QuizListView, QuestionListView

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<category>/', QuizListView.as_view()),
    path('<category>/<title>/', QuestionListView.as_view()),
]