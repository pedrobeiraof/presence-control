from django.urls import path

from . import views

urlpatterns = [
    path('recognition/', views.Reconhecimento.as_view()),
]