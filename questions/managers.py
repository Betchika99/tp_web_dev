from django.db import models


class QuestionManager(models.Manager):

    def new_questions(self):
        return self.all().order_by('-create_date')

    def popular(self):
        return self.all().order_by('-rating')


class TagManager(models.Manager):

    def get_by_tag(self, tag_name):
        return self.get(title=tag_name).question_set.all().order_by('-create_date')
