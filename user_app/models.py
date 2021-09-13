from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserResponse(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='usermodel')
    quizid=models.CharField(max_length=100)
    score=models.IntegerField()
    timetaken=models.IntegerField()
    result=models.CharField(max_length=200)
    def getuserresponse(self):
        return self.questions_set.all()

class QuestionsList(models.Model):
    quizname=models.ForeignKey(UserResponse,on_delete=models.CASCADE,related_name="questions_set")
    questionid=models.IntegerField()
    def getquestionlist(self):
        return self.response_set.all()

class ResponseList(models.Model):
    answerid=models.IntegerField()
    questionname=models.ForeignKey(QuestionsList,on_delete=models.CASCADE,related_name="response_set")
