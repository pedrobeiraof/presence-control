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
	tipo = serializers.SerializerMethodField()

	class Meta:
		model = Aula
		fields = '__all__'
		depth = 2

	def get_tipo(self, obj):
		data_atual = int(datetime.datetime.now().strftime("%Y%m%d%H%M"))
		data_inicio = int(obj.data_inicio.strftime("%Y%m%d%H%M"))
		data_final = int(obj.data_final.strftime("%Y%m%d%H%M"))
		if data_atual < data_inicio:
			return 1
		if data_atual > data_inicio and data_atual < data_final:
			return 2
		return 3

