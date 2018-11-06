from django.core.management.base import BaseCommand
from questions.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = self.add_users()
        tags = self.add_tags()
        questions_count = 2
        answers_count = 2
        for i in range(questions_count):
            que_title = 'Тестовый вопрос ' + str(i)
            que_text = 'Guys, i have a trouble with a moon park. Can not find th black-jack...'
            q = Question.objects.create(title=que_title, author=users[0], text=que_text)
            q.tags.add(tags[i])
            q.tags.add(tags[i+1])
            for j in range(answers_count):
                ans_title = 'Тестовый ответ ' + str(j)
                Answer.objects.create(text=ans_title, author=users[1], question=q)
        self.stdout.write(self.style.SUCCESS('Successfully added'))

    def add_users(self):
        users = []
        u = User.objects.create(username="Test User", email="test@test.ru", password='123')
        users.append(u)
        u = User.objects.create(username="Test User 2", email="test2@test.ru", password='1234')
        users.append(u)
        return users

    def add_tags(self):
        tags = []
        t = Tag.objects.create(title="python")
        tags.append(t)
        t = Tag.objects.create(title="MySQL")
        tags.append(t)
        t = Tag.objects.create(title="django")
        tags.append(t)
        t = Tag.objects.create(title="Mail.Ru")
        tags.append(t)
        t = Tag.objects.create(title="Firefox")
        tags.append(t)
        return tags
