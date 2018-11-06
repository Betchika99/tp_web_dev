from django.urls import path
from questions import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hottest, name="hot"),
    path("tag/<str:tag_title>/", views.by_tag, name="tag"),
    path('question/<int:number>', views.question, name='question'),
    path("login/", views.login, name="login"),
    path("signup/", views.register, name="signup"),
    path("ask/", views.ask, name="add_question"),
]

