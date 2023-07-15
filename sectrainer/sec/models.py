from django.db import models

# Create your models here.


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, unique=True)
    question_chapter = models.CharField(max_length=64)
    question_number = models.IntegerField()
    question_source = models.CharField(max_length=64)
    question_value = models.TextField(max_length=4096)
    question_img = models.CharField(max_length=64)

    choice_a = models.CharField(max_length=1024)
    choice_b = models.CharField(max_length=1024)
    choice_c = models.CharField(max_length=1024)
    choice_d = models.CharField(max_length=1024)

    correct_answer = models.CharField(max_length=1)

    explanation = models.TextField(max_length=4096)
