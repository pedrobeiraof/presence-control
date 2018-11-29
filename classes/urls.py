from django.urls import path

from . import views

urlpatterns = [
    path('aulas', views.ListAulas.as_view()),
    path('aulas/<int:pk>', views.RetrieveAulas.as_view()),
    path('alunos', views.ListAlunos.as_view()),
    path('relatorio', views.RetrieveRelatorio.as_view()),
]