from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"lastest_question_list": lastest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id) -> HttpResponse:
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id) -> HttpResponse:
    response = "Your're looking at question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id) -> HttpResponse:
    return HttpResponse("Your're voting on question %s." % question_id)
