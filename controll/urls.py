from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_all),
    path('add', views.add_aluno),
    path('start', views.start_aula),
    path('end', views.end_aula),
    path('get-alunos', views.get_alunos),
]