from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question,Choice
from django.template import loader
from django.http import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    # output=','.join([q.question_text for q in latest_question_list])
    context={
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except:
        raise Http404("问题不存在")
    return render(request,'polls/detail.html',{'question':question})


def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',
                      {
                          'question':question,
                          'error_message':'您没有选择选项'
                      })
    else:
        selected_choice.vote+=1;
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results',args=(question.id,)))

    # return HttpResponse("你下在投票：%s." % question_id)

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{'question':question})

