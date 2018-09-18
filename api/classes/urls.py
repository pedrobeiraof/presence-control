from django.urls import path

from . import views

urlpatterns = [
    path('alunos', views.ListAlunos.as_view()),
]