from tkinter import CASCADE
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='quizes')

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.TextField()
    DIFFICULTY = (
        ('E', 'Easy'),
        ('N', 'Normal'),
        ('H', 'Hard'),
    )
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY, default='N')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')


class Answer(models.Model):
    answer_text = models.TextField()
    is_right = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')


    