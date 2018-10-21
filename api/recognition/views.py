from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Aluno, Aula, Momento
import face_recognition
from PIL import Image
from io import BytesIO


class Reconhecimento(APIView):

	def generate_encodings(self, aluno):
		known_image = face_recognition.load_image_file(aluno.foto)
		return face_recognition.face_encodings(known_image)[0]

	def post(self, request):
		imagem = request.FILES.get('imagem', None)
		id_aula = request.data.get('id_aula', None)
		# link_img = request.data.get('imagem', None)

		if imagem:
			aula = Aula.objects.filter(id=id_aula).first()
			if aula:
				alunos = aula.alunos.all()
				encoding_list = [self.generate_encodings(aluno) for aluno in alunos]
				unknown_image = face_recognition.load_image_file(imagem)
				unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

				results = face_recognition.compare_faces(encoding_list, unknown_encoding)

				data = []
				momento = Momento(aula_id=aula.id)
				momento.save()

				for idx, result in enumerate(results):
					if result:
						data.append(alunos[idx].id)
						momento.alunos_presentes.add(alunos[idx])
				momento.save()
				return Response(data=data)
			return Response(data='Aula não encontrada', status=404)
		return Response(data='Imagem inválida', status=400)
