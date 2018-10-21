from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.models import Aluno, Aula
import datetime

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class AulasSerializer(ModelSerializer):
	data_inicio = serializers.DateTimeField(format='%H:%M %d/%m/%Y')
	data_final = serializers.DateTimeField(format='%H:%M  %d/%m/%Y')
	is_atual = serializers.SerializerMethodField(read_only=True)

	class Meta:
		model = Aula
		fields = '__all__'
		depth = 2

	def get_is_atual(self, obj):
		import pdb; pdb.set_trace()
