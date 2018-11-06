# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from questions.managers import *


class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Время регистрации")
    rating = models.IntegerField(default=0, verbose_name=u"Рейтинг")


class Tag(models.Model):
    title = models.CharField(max_length=70, unique=True, verbose_name=u"Заголовок ярлыка")

    objects = TagManager()

    def __str__(self):
        return self.title


class Like(models.Model):
    LIKE = 1
    DISLIKE = -1
    vote = models.SmallIntegerField(verbose_name=u"Голос", default=LIKE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Question(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name=u"Автор")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")
    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    tags = models.ManyToManyField(Tag, blank=True)
    rating = models.IntegerField(default=0, null=False, verbose_name=u'Рейтинг')
    likes = GenericRelation(Like, related_query_name='questions')

    objects = QuestionManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Answer(models.Model):
    text = models.TextField(verbose_name=u"Текст ответа")
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, verbose_name=u"Автор")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата написания")
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE, verbose_name=u"Вопрос")
    is_right = models.BooleanField(default=False, verbose_name=u"Правильный ответ")
    rating = models.IntegerField(default=0, null=False, verbose_name=u'Рейтинг')
    likes = GenericRelation(Like, related_query_name='answers')

    def __str__(self):
        return self.text
