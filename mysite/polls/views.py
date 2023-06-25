from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    try:
        question = Question.objects.filter(id=question_id).get()
        return HttpResponse(question.question_text)
    except ObjectDoesNotExist:
        return HttpResponse('ВОПРОС НЕ НАЙДЕМ')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
