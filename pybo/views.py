from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from.models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    q_list = Question.objects.order_by('-create_date') #query날리는 것과 같음
    return render(request, 'pybo/question_list.html',{'question_list' : q_list }) #render이라는 함수를 이용해서 화면에 뿌림.


def detail(request,question_id):
    q = get_object_or_404(Question, pk=question_id) #어떤 값으로 조회할래? => pk
    return render(request, 'pybo/question_detail.html', {
        'question' : q })
    
@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST": # 정상적인 경우
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False) #commit은 아직 대기해줘! => commit 하면 되돌릴 수 없기 때문에
            answer.author = request.user # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            redirect('pybo:detail', question_id = question.id) #실행 후에 다시 main으로 보내기
    else: # 비정상적인 경우
        form = AnswerForm()
    context = {'question' : question, 'form' : form} # question이라는 keyword로 formdata를 넘기기
    return render(request, 'pybo/question_detail.html', context) # 렌더링 하기

@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form' : form }
    return render(request, 'pybo/question_form.html', context)




    #return HttpResponse("4월 10일 월요일")
    
    #주소를 만들고 주소에 해당하는 함수를 만들고 화면 호출이 순서
