from unicodedata import category
from rest_framework import serializers
from .models import Category, Quiz, Question, Answer
from pprint import pprint

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

    def create(self, validated_data):
        #! Altteki 3 satırda url üzerinden category_name e ulaştım
        url_str = str(self.context['request'])
        first = url_str[:-3].rfind('/') + 1
        category_name =  url_str[first:-3]
        cat_id = Category.objects.get(name__iexact=category_name).id
        validated_data['category_id'] = cat_id
        quiz = Quiz.objects.create(**validated_data)
        quiz.save()
        return quiz


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer_text', 'is_right')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('title', 'difficulty', 'answers')

    def create(self, validated_data):
        #! Altteki 3 satırda url üzerinden quiz_title e ulaşmaya çalıştım
        url_str = str(self.context['request'])
        first = url_str[:-3].rfind('/') + 1
        quiz_title =  url_str[first:-3]
        quiz_id = Quiz.objects.get(title__iexact=quiz_title).id
        validated_data['quiz_id'] = quiz_id
        answer_data = validated_data.pop('answers')
        question = Question.objects.create(**validated_data)
        for answer in answer_data:
            question_id = question.id
            ans = Answer.objects.create(**answer, question_id=question_id)
            ans.save()
            question.answers.add(ans)
        question.save()
        return question
