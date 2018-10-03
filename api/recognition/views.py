from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Aluno
import face_recognition


class Reconhecimento(APIView):

	def generate_encodings(self, aluno):
		known_image = face_recognition.load_image_file(aluno.foto)
		return face_recognition.face_encodings(known_image)[0]

	def post(self, request):
		imagem = request.FILES['imagem']

		if imagem:
			alunos = Aluno.objects.all()
			encoding_list = [self.generate_encodings(aluno) for aluno in alunos]
			unknown_image = face_recognition.load_image_file(imagem)
			unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

			results = face_recognition.compare_faces(encoding_list, unknown_encoding)
			return Response(data=results)
		return Response(data='Imagem inválida')
