from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#database를 만들 때 models.py로 들어가기

#Question, Answer = table 
#subject,content,create_date = columns
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,
on_delete=models.CASCADE) #질문이 삭제되면 연결되어있는 대답도 삭제가 되는 기능 
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.question
