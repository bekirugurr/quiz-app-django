from django.urls import path, include
from .views import CategoryListCreateView, QuizListCreateView, QuestionListCreateView,CategoryGetUpdateDeleteView, QuizGetUpdateDeleteView, QuestionGetUpdateDeleteView, AnswerGetUpdateDeleteView

urlpatterns = [
    path('nested_admin/', include('nested_admin.urls')),
    path('', CategoryListCreateView.as_view()),
    path('category_id/<int:id>/', CategoryGetUpdateDeleteView.as_view()),
    path('<category>/', QuizListCreateView.as_view()),
    path('quiz_id/<int:id>/', QuizGetUpdateDeleteView.as_view()),
    path('question_id/<int:id>/', QuestionGetUpdateDeleteView.as_view()), # iki alttaki satırdan aşağıda olursa çalışmıyor
    path('answer_id/<int:id>/', AnswerGetUpdateDeleteView.as_view()), # alttaki satırdan aşağıda olursa çalışmıyor
    path('<category>/<title>/', QuestionListCreateView.as_view()),

]