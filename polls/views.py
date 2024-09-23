# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone 
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
# def index(request): 템플릿에 context 변수 전달한 Question 모델 객체
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj} # question_list는 페이징 객체(page_obj)
    return render(request, 'polls/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    #answer.save()
    return redirect('polls:detail', question_id=question.id)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('polls:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'polls/question_form.html', context)