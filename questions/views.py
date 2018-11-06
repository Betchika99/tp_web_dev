# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from questions.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404


def paginate(request, objects_list):
    paginator = Paginator(objects_list, 2)
    try:
        page = paginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        page = paginator.get_page(1)
    except EmptyPage:
        page = paginator.get_page(paginator.num_pages)
    return page


def index(request):
    questions = paginate(request, Question.objects.new_questions())
    return render(request, "index.html", context={"questions": questions})


def question(request, number):
    return render(request, "question.html", context={"q": get_object_or_404(Question, pk=number)})


def hottest(request):
    questions = paginate(request, Question.objects.popular())
    return render(request, "hot.html", context={"questions": questions})


def by_tag(request, tag_title):
    questions = paginate(request, Tag.objects.get_by_tag(tag_title))
    return render(request, "tag.html", context={"questions": questions, "tag": tag_title})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def ask(request):
    return render(request, "ask.html")
