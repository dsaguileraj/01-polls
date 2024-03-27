from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from .models import Question, Choice
from .forms import CreateQuestion


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return redirect(reverse("polls:results", args=(question_id,)))


def post(request):
    if request.method == "POST":
        form = CreateQuestion(request.POST)
        if form.is_valid():
            Question.objects.create(question_text = request.POST["question_text"], pub_date = timezone.now())
            return redirect(reverse_lazy("polls:index"))

    context = {
        "form": CreateQuestion(),
    }
    return render(request, "polls/post.html", context)