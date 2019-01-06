from django import forms
from questions import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,
                               min_length=1)
    password = forms.CharField(max_length=128,
                               min_length=1,
                               widget=forms.PasswordInput())

    @property
    def username_value(self):
        return self.cleaned_data['username']

    @property
    def password_value(self):
        return self.cleaned_data['password']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        exclude = ['is_active', 'author', 'create_date']

    def save(self, author_id, commit=True):
        instance = super().save(commit=False)
        instance.author_id = author_id
        instance.save()
        return instance


"""
class QuestionForm(forms.ModelForm):
    tag = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'long'})

    def clean_tags(self):
        tags_str = self.cleaned_data.get('tag')

        # tags = []
        # for tag in tags_str.split(' , '):
        #    tags += tag.strip()
        # ниже код короче

        tags = [tag.strip() for tag in tags_str.split(' , ') if tag.strip()]  # на выходе list
        if len(tags):
            reise forms.ValidationError("Нужны теги")

    class Meta:
        model = Question
        exclude = ['is_active', 'author', 'create_date']
"""
