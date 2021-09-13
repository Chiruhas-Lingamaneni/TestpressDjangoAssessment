#from _typeshed import Self
from django.db import models
import random

# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=50)
    number_of_questions=models.IntegerField()
    score_to_pass=models.IntegerField()
    difficulity=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Quizzes"
    def get_questions(self):
        questions=list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

class Questions(models.Model):
    question=models.CharField(max_length=1000)
    quiz=models.ManyToManyField(Quiz,related_name="question_set")

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural="Questions"
    def get_answers(self):
        return self.answer_set.all()

class Answers(models.Model):
    option=models.CharField(max_length=100)
    correct=models.BooleanField()
    question=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name="answer_set")

    def __str__(self):
        return f' option {self.option} correct {self.correct}'
    class Meta:
        verbose_name_plural="Answers"