from rest_framework import serializers
from .models import Category, Quiz, Question, Answer

class CategorySerializer(serializers.ModelSerializer):
    quiz_count =  serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count')

    def get_quiz_count(self, obj):
        return obj.quizes.count()

class QuizSerializer(serializers.ModelSerializer):

    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('title', 'question_count')

    def get_question_count(self, obj):
        return obj.questions.count()



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_text', 'is_right')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('title', 'difficulty', 'answers')
