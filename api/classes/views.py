from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from core.models import Aluno, Aula
from .serializers import AlunosSerializer, AulasSerializer

class ListAlunos(ListCreateAPIView):
	queryset = Aluno.objects.all()
	serializer_class = AlunosSerializer


class ListAulas(ListCreateAPIView):
	queryset = Aula.objects.all()
	serializer_class = AulasSerializer	


class RetrieveAulas(RetrieveAPIView):
	queryset = Aula.objects.all()
	serializer_class = AulasSerializer

