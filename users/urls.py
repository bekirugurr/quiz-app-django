from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
]

