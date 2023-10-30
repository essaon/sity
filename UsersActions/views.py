from django.http import Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from . import models


def index(request):

    latest_question = models.Questions.objects.order_by('-publish_date')[:5]
    context = {'latest_question': latest_question}
    return render(request, 'home.html', context)


def details(request, question_id):
    try:
        question = models.Questions.objects.get(pk=question_id)
    except models.Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})


def result(request, question_id):
    question = get_object_or_404(models.Questions, pk=question_id)
    return render(request, 'result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(models.Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question, 'error_message': "You didnt select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
