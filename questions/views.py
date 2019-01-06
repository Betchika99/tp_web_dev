# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import (
    render,
    redirect,
    reverse,
)
from django.views.decorators.http import require_POST

from questions.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.contrib import auth
from questions import forms
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse


def paginate(request, objects_list):
    paginator = Paginator(objects_list, 2)
    try:
        page = paginator.get_page(request.GET.get('page'))
    except PageNotAnInteger:
        page = paginator.get_page(1)
    except EmptyPage:
        page = paginator.get_page(paginator.num_pages)
    return page


@login_required
def index(request):
    questions = paginate(request, Question.objects.new_questions())
    return render(request, "index.html", context={"questions": questions})


@login_required
def question(request, number):
    return render(request, "question.html", context={"q": get_object_or_404(Question, pk=number)})


@login_required
def hottest(request):
    questions = paginate(request, Question.objects.popular())
    return render(request, "hot.html", context={"questions": questions})


def by_tag(request, tag_title):
    questions = paginate(request, Tag.objects.get_by_tag(tag_title))
    return render(request, "tag.html", context={"questions": questions, "tag": tag_title})


def login(request):
    form = forms.LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                user = User.objects.get(username=form.username_value)

                if user.check_password(form.password_value):
                    auth.login(request, user)
                    redirect_url = request.GET.get('next') or reverse('questions:index')
                    return redirect(redirect_url)
                else:
                    form.add_error(None, 'Неверный логин или пароль')

            except User.DoesNotExist:
                form.add_error('username', 'Ты кто такой?')

    return render(request, "login.html", {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('questions:login')


def register(request):
    return render(request, "register.html")


def ask(request):
    form = forms.QuestionForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            q = form.save(author_id=request.user.id)
            return redirect(reverse('questions:question', kwargs={'number': q.pk}))

    return render(request, "ask.html", {'form': form})

@require_POST
@login_required
def like_question(request):
    if request.is_ajax():
        return JsonResponse(400)

    try:
        data = json.loads(request.body)
        like = data['like']

        if like not in [Like.LIKE, Like.DISLIKE]:
            raise ValueError('Неверный тип лайка')

        question_id = data['question_id']
    except Exception as e:
        return JsonResponse(data={'status': 'error', 'message': str(e)}, status=400)

    question = get_object_or_404(Question, pk=question_id)

    try:
        Like.objects.create(author=request.user,
                            vote=like,
                            content_object=question)
        return JsonResponse(data={'status': 'success', 'message': 'OK'}, status=200)
    except Exception as e:
        return JsonResponse(data={'status': 'error', 'message': 'Невозможно поставить лайк'}, status=400)
