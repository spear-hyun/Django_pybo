from django import forms #django에서 만든 기능 forms (유명함)
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm): #괄호 안에 있는게 상속
    class Meta:
        model = Question
        fields = ['subject', 'content']
        
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {'content':'답변내용'}