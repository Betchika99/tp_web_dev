# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from questions.models import *
from django.contrib import admin

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Like)
# Register your models here.
