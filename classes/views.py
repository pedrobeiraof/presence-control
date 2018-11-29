from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from core.models import Aluno, Aula, Momento
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


class RetrieveRelatorio(APIView):

	def get(self, request):
		aula_id = request.query_params.get('aula_id', None)
		momentos = Momento.objects.filter(aula_id=aula_id).all()

		alunos_momento = {}

		for momento in momentos:
			alunos_presentes = momento.alunos_presentes.all()
			for aluno in alunos_presentes:
				if alunos_momento.get(aluno.nome, None):
					alunos_momento[aluno.nome] += 1
				else:
					alunos_momento[aluno.nome] = 1

		alunos_list = [aluno for aluno in alunos_momento]

		result = []
		nr_total = len(momentos)
		for aluno in alunos_list:
			nr_parcial = alunos_momento[aluno]
			porcentagem = round((nr_parcial / nr_total if nr_total > 0 else 0) * 100, 2)
			result.append(dict(
				aluno=aluno,
				porcentagem=f'{porcentagem}%',
				presente=porcentagem > 70
			))


		return Response(data=result)
