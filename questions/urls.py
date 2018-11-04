from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.base, name='base'),
]