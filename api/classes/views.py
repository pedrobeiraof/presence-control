from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import Aluno
from .serializers import AlunosSerializer

class ListAlunos(ListCreateAPIView):
	queryset = Aluno.objects.all()
	serializer_class = AlunosSerializer
