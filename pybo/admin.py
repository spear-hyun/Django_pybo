from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)#admin에 있는 question 모델을 site에 등록
admin.site.register(Answer)

# Register your models here.
