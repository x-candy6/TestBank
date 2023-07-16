from django.db import models

# Create your models here.
class Question(models.Model):
    questionid = models.AutoField(db_column='QuestionID', primary_key=True)  # Field name made lowercase.
    chapter = models.CharField(db_column='Source', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=100, blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(db_column='Media', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True, null=True)  # Field name made lowercase.
    b = models.TextField(db_column='B', blank=True, null=True)  # Field name made lowercase.
    c = models.TextField(db_column='C', blank=True, null=True)  # Field name made lowercase.
    d = models.TextField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    correctanswer = models.TextField(db_column='CorrectAnswer', blank=True, null=True)  # Field name made lowercase.
    explanation = models.TextField(db_column='Explanation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question'