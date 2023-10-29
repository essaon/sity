from django.shortcuts import render
from . import models


def index(request):

    latest_question = models.Questions.objects.order_by('-publish_date')[:5]
    context = {'latest_question': latest_question}
    return render(request, 'home.html', context)
