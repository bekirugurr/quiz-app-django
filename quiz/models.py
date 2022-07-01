from tkinter import CASCADE
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizes')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = "Quizzes"

class Question(models.Model):
    title = models.CharField(max_length=100)
    DIFFICULTY = (
        ('E', 'Easy'),
        ('N', 'Normal'),
        ('H', 'Hard'),
    )
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY, default='N')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name_plural = "Questions"


class Answer(models.Model):
    answer_text = models.CharField(max_length=80)
    is_right = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    class Meta:
        verbose_name_plural = "Answers"


    