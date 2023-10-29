from django.http import Http404
from django.shortcuts import render

from sity.UsersActions.admin import QuestionAdmin
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
    return render(request, 'result.html', {'question': question})
