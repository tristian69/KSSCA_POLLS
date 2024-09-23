# from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
# def index(request): 템플릿에 context 변수 전달한 Question 모델 객체
def index(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question':question}
    return render(request, 'polls/question_detail.html', context)

